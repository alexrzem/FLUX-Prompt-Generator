"""
Image Caption Service using Florence-2 model
"""
import torch
from transformers import AutoModelForCausalLM, AutoProcessor
from PIL import Image
import sys

class ImageCaptionService:
    def __init__(self):
        self.model = None
        self.processor = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = "microsoft/Florence-2-large"
        self.initialized = False

    def initialize(self):
        """Lazy initialization of the model"""
        if self.initialized:
            return

        try:
            print(f"Loading Florence-2 model on {self.device}...", file=sys.stderr)
            self.processor = AutoProcessor.from_pretrained(
                self.model_name,
                trust_remote_code=True
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                trust_remote_code=True
            ).to(self.device)
            self.initialized = True
            print("Florence-2 model loaded successfully", file=sys.stderr)
        except Exception as e:
            print(f"Error loading Florence-2 model: {str(e)}", file=sys.stderr)
            raise

    def generate_caption(self, image: Image.Image) -> str:
        """
        Generate a detailed caption for the given image

        Args:
            image: PIL Image object

        Returns:
            Generated caption string
        """
        if not self.initialized:
            self.initialize()

        try:
            # Prepare inputs
            prompt = "<MORE_DETAILED_CAPTION>"
            inputs = self.processor(
                text=prompt,
                images=image,
                return_tensors="pt"
            ).to(self.device)

            # Generate caption
            with torch.no_grad():
                generated_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=1024,
                    num_beams=3,
                    do_sample=False
                )

            # Decode the generated text
            generated_text = self.processor.batch_decode(
                generated_ids,
                skip_special_tokens=True
            )[0]

            # Extract the caption from the generated text
            # Florence-2 returns the prompt followed by the caption
            caption = generated_text.replace(prompt, "").strip()

            return caption

        except Exception as e:
            print(f"Error generating caption: {str(e)}", file=sys.stderr)
            raise
