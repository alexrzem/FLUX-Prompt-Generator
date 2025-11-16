"""
OpenAI Service for prompt enhancement
"""
import os
from openai import OpenAI
import sys

class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = None

        if self.api_key:
            try:
                self.client = OpenAI(api_key=self.api_key)
                print("OpenAI client initialized", file=sys.stderr)
            except Exception as e:
                print(f"Error initializing OpenAI client: {str(e)}", file=sys.stderr)

    def is_available(self) -> bool:
        """Check if OpenAI API is available"""
        return self.client is not None

    def enhance_prompt(
        self,
        prompt: str,
        happy_talk_mode: bool = False,
        compression_level: str = 'none',
        movie_poster_mode: bool = False,
        custom_instruction: str = ''
    ) -> str:
        """
        Enhance the given prompt using OpenAI GPT-4

        Args:
            prompt: The original prompt to enhance
            happy_talk_mode: If True, make the prompt more upbeat and positive
            compression_level: Level of compression ('none', 'light', 'medium', 'heavy')
            movie_poster_mode: If True, format for movie poster style
            custom_instruction: Additional custom instructions

        Returns:
            Enhanced prompt
        """
        if not self.is_available():
            raise Exception("OpenAI API is not available")

        # Build system message based on options
        system_parts = []

        base_instruction = """You are an expert prompt engineer for text-to-image AI models like FLUX.
Your task is to enhance and improve image generation prompts to make them more detailed,
creative, and effective while maintaining the core intent."""

        system_parts.append(base_instruction)

        if happy_talk_mode:
            system_parts.append(
                "Use an upbeat, positive, and enthusiastic tone. "
                "Add vibrant, joyful, and optimistic descriptors."
            )

        if movie_poster_mode:
            system_parts.append(
                "Format the prompt in a cinematic, movie poster style. "
                "Include dramatic lighting, composition, and atmosphere suitable for a movie poster."
            )

        compression_instructions = {
            'light': "Make the prompt slightly more concise while keeping key details.",
            'medium': "Significantly reduce the prompt length, keeping only the most important elements.",
            'heavy': "Compress the prompt to essential elements only, minimal words with maximum impact."
        }

        if compression_level in compression_instructions:
            system_parts.append(compression_instructions[compression_level])

        if custom_instruction:
            system_parts.append(f"Additional instruction: {custom_instruction}")

        system_message = "\n\n".join(system_parts)

        user_message = f"""Please enhance this image generation prompt:

{prompt}

Provide only the enhanced prompt without any explanations or additional text."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=1000
            )

            enhanced_prompt = response.choices[0].message.content.strip()
            return enhanced_prompt

        except Exception as e:
            print(f"Error enhancing prompt: {str(e)}", file=sys.stderr)
            raise
