from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from PIL import Image
import io
import base64

# Import AI services
from services.image_caption import ImageCaptionService
from services.translator import TranslatorService
from services.openai_service import OpenAIService

app = Flask(__name__)
CORS(app)

# Initialize services
caption_service = ImageCaptionService()
translator_service = TranslatorService()
openai_service = OpenAIService()

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Backend is running'}), 200

@app.route('/api/openai-status', methods=['GET'])
def check_openai():
    """Check if OpenAI API is available"""
    return jsonify({'available': openai_service.is_available()}), 200

@app.route('/api/caption', methods=['POST'])
def generate_caption():
    """Generate image caption using Florence-2"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400

        image_file = request.files['image']

        # Read and process image
        image_bytes = image_file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Generate caption
        caption = caption_service.generate_caption(image)

        return jsonify({'caption': caption}), 200

    except Exception as e:
        print(f"Error generating caption: {str(e)}", file=sys.stderr)
        return jsonify({'error': str(e)}), 500

@app.route('/api/translate', methods=['POST'])
def translate_text():
    """Translate text from one language to another"""
    try:
        data = request.get_json()

        if 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400

        text = data['text']
        source_lang = data.get('source_lang', 'ko')
        target_lang = data.get('target_lang', 'en')

        # Translate text
        translated = translator_service.translate(text, source_lang, target_lang)

        return jsonify({'translated_text': translated}), 200

    except Exception as e:
        print(f"Error translating text: {str(e)}", file=sys.stderr)
        return jsonify({'error': str(e)}), 500

@app.route('/api/enhance', methods=['POST'])
def enhance_prompt():
    """Enhance prompt using OpenAI"""
    try:
        data = request.get_json()

        if 'prompt' not in data:
            return jsonify({'error': 'No prompt provided'}), 400

        prompt = data['prompt']
        happy_talk_mode = data.get('happy_talk_mode', False)
        compression_level = data.get('compression_level', 'none')
        movie_poster_mode = data.get('movie_poster_mode', False)
        custom_instruction = data.get('custom_instruction', '')

        # Enhance prompt
        enhanced = openai_service.enhance_prompt(
            prompt,
            happy_talk_mode=happy_talk_mode,
            compression_level=compression_level,
            movie_poster_mode=movie_poster_mode,
            custom_instruction=custom_instruction
        )

        return jsonify({'enhanced_prompt': enhanced}), 200

    except Exception as e:
        print(f"Error enhancing prompt: {str(e)}", file=sys.stderr)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting FLUX Prompt Generator Backend...")
    print(f"OpenAI Available: {openai_service.is_available()}")
    app.run(host='0.0.0.0', port=5000, debug=True)
