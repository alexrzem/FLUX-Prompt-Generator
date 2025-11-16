# FLUX Prompt Generator

A modern Vue.js application for generating detailed prompts for FLUX image generation, ported from the original Python Gradio application.

## Features

- **Comprehensive Prompt Generation**: Create detailed prompts with customizable components including artform, character settings, scene elements, and style preferences
- **AI-Powered Image Captioning**: Upload images to generate captions using the Florence-2 vision model
- **Korean Language Support**: Type Korean text in prompts with automatic translation to English
- **OpenAI Enhancement**: Enhance prompts using GPT-4 with options for happy talk mode, compression, and movie poster styling
- **Reproducible Results**: Use seed values to generate identical prompts with the same settings
- **Modern UI**: Built with Vue 3, PrimeVue components, and TailwindCSS

## Architecture

### Frontend
- **Vue 3** with Composition API
- **PrimeVue** for UI components
- **TailwindCSS** for styling
- **Vite** for fast development and building

### Backend
- **Flask** Python server
- **Florence-2** model for image captioning
- **Helsinki-NLP Opus** models for translation
- **OpenAI GPT-4** for prompt enhancement

## Project Structure

```
FLUX-Prompt-Generator/
├── backend/
│   ├── services/
│   │   ├── image_caption.py      # Florence-2 image captioning
│   │   ├── translator.py         # Language translation
│   │   └── openai_service.py     # OpenAI prompt enhancement
│   ├── app.py                    # Flask application
│   └── requirements.txt          # Python dependencies
├── public/
│   └── data/                     # JSON data files for prompt components
├── src/
│   ├── services/
│   │   └── api.js                # API integration layer
│   ├── utils/
│   │   └── PromptGenerator.js    # Core prompt generation logic
│   ├── App.vue                   # Main application component
│   ├── main.js                   # Vue application entry point
│   └── style.css                 # Global styles
├── index.html                    # HTML entry point
├── package.json                  # Node.js dependencies
├── vite.config.js                # Vite configuration
└── tailwind.config.js            # TailwindCSS configuration
```

## Installation

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+
- CUDA-capable GPU (optional, for faster AI processing)

### Frontend Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

### Backend Setup

1. Create a Python virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (optional):
```bash
# Create a .env file in the backend directory
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

4. Start the backend server:
```bash
python app.py
```

The backend will be available at `http://localhost:5000`

## Usage

1. **Generate a Basic Prompt**:
   - Enter a subject or custom prompt
   - Click "Generate Prompt"
   - The generated prompt appears in the middle panel

2. **Customize Your Prompt**:
   - Use the accordion sections to select specific attributes
   - Choose "Random" to let the generator pick values automatically
   - Choose "None" to exclude a category

3. **Image Captioning**:
   - Upload an image in the middle panel
   - The Florence-2 model will generate a detailed caption
   - Click "Use as Custom Prompt" to incorporate the caption

4. **Translate Korean Text**:
   - Type Korean text in the custom prompt field
   - The system will automatically translate it during generation

5. **Enhance with AI** (requires OpenAI API key):
   - Generate a prompt first
   - Configure enhancement options in the right panel
   - Click "Enhance with AI" to improve the prompt using GPT-4

6. **Reproducible Generation**:
   - Set a specific seed value
   - Use the same seed with identical settings to generate the same prompt

## Configuration

### OpenAI API Key
To enable AI prompt enhancement, set your OpenAI API key as an environment variable:

**Linux/Mac:**
```bash
export OPENAI_API_KEY=your-api-key-here
```

**Windows:**
```bash
set OPENAI_API_KEY=your-api-key-here
```

Or create a `.env` file in the `backend` directory:
```
OPENAI_API_KEY=your-api-key-here
```

### GPU Acceleration
The backend will automatically use CUDA if available. To disable GPU usage:
```python
# In backend/services/*.py, change:
self.device = "cpu"
```

## Data Files

The application uses JSON data files located in `public/data/` containing predefined options for:
- Artforms and photography types
- Character attributes (body types, roles, hairstyles, clothing, poses)
- Scene elements (backgrounds, places, lighting)
- Style settings (composition, photography styles, framing)
- Artists and photographers
- Devices and digital artforms

You can customize these files to add your own options.

## Development

### Frontend Development
```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
```

### Backend Development
```bash
cd backend
python app.py    # Start Flask server with auto-reload
```

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/openai-status` - Check OpenAI availability
- `POST /api/caption` - Generate image caption (multipart/form-data with image file)
- `POST /api/translate` - Translate text
- `POST /api/enhance` - Enhance prompt with OpenAI

## Troubleshooting

### Models Not Loading
If AI models fail to load:
1. Ensure you have enough disk space (models are ~2-5GB each)
2. Check your internet connection (first run downloads models)
3. Try using CPU if GPU memory is insufficient

### CORS Errors
If you encounter CORS errors:
1. Ensure the backend is running on port 5000
2. Check the proxy configuration in `vite.config.js`

### OpenAI API Errors
If OpenAI features don't work:
1. Verify your API key is set correctly
2. Check your OpenAI account has credits
3. Ensure you're using a valid API key format

## Credits

This application is a Vue.js port of the original [FLUX-Prompt-Generator](https://huggingface.co/spaces/ginipick/FLUX-Prompt-Generator) by gokaygokay and ginipick.

### Technologies Used
- Vue.js 3
- PrimeVue
- TailwindCSS
- Flask
- Florence-2 (Microsoft)
- Helsinki-NLP Opus MT
- OpenAI GPT-4

## License

Apache 2.0 License (following the original project)
