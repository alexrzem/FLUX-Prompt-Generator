"""
Translation Service using Helsinki-NLP Opus models
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import sys

class TranslatorService:
    def __init__(self):
        self.models = {}
        self.tokenizers = {}
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def get_model_name(self, source_lang: str, target_lang: str) -> str:
        """Get the appropriate model name for the language pair"""
        # Map of language pairs to model names
        model_map = {
            ('ko', 'en'): 'Helsinki-NLP/opus-mt-ko-en',
            ('en', 'ko'): 'Helsinki-NLP/opus-mt-en-ko',
            ('ja', 'en'): 'Helsinki-NLP/opus-mt-ja-en',
            ('en', 'ja'): 'Helsinki-NLP/opus-mt-en-ja',
            ('zh', 'en'): 'Helsinki-NLP/opus-mt-zh-en',
            ('en', 'zh'): 'Helsinki-NLP/opus-mt-en-zh',
        }

        return model_map.get((source_lang, target_lang))

    def load_model(self, source_lang: str, target_lang: str):
        """Load translation model for the specified language pair"""
        model_name = self.get_model_name(source_lang, target_lang)

        if not model_name:
            raise ValueError(f"Translation not supported for {source_lang} -> {target_lang}")

        # Check if model is already loaded
        if model_name in self.models:
            return

        try:
            print(f"Loading translation model: {model_name}", file=sys.stderr)
            self.tokenizers[model_name] = AutoTokenizer.from_pretrained(model_name)
            self.models[model_name] = AutoModelForSeq2SeqLM.from_pretrained(
                model_name
            ).to(self.device)
            print(f"Translation model loaded: {model_name}", file=sys.stderr)
        except Exception as e:
            print(f"Error loading translation model: {str(e)}", file=sys.stderr)
            raise

    def translate(self, text: str, source_lang: str = 'ko', target_lang: str = 'en') -> str:
        """
        Translate text from source language to target language

        Args:
            text: Text to translate
            source_lang: Source language code (e.g., 'ko', 'en')
            target_lang: Target language code (e.g., 'en', 'ko')

        Returns:
            Translated text
        """
        # Load model if not already loaded
        self.load_model(source_lang, target_lang)

        model_name = self.get_model_name(source_lang, target_lang)
        tokenizer = self.tokenizers[model_name]
        model = self.models[model_name]

        try:
            # Tokenize input
            inputs = tokenizer(text, return_tensors="pt", padding=True).to(self.device)

            # Generate translation
            with torch.no_grad():
                translated = model.generate(**inputs, max_length=512)

            # Decode translation
            translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

            return translated_text

        except Exception as e:
            print(f"Error translating text: {str(e)}", file=sys.stderr)
            raise
