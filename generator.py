from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

class TextureGenerator:

    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/stable-diffusion-2-1-base",
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )

        self.pipe = self.pipe.to(self.device)

    def generate_texture(self, block_name: str, resolution: int, style: str):

        prompt = f"""
        seamless pixel art {block_name} texture,
        top down view,
        tileable,
        flat shading,
        no shadows,
        no perspective,
        {style} style,
        game texture
        """

        image = self.pipe(prompt).images[0]

        # Resize to exact pixel size
        image = image.resize((resolution, resolution), Image.NEAREST)

        return image