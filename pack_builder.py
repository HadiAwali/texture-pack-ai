import os
import json
import zipfile
from PIL import Image

class PackBuilder:

    def __init__(self, pack_name="AI_Texture_Pack"):
        self.pack_name = pack_name
        self.base_path = f"output/{pack_name}"
        self.texture_path = os.path.join(
            self.base_path,
            "assets/minecraft/textures/block"
        )

    def create_structure(self):
        os.makedirs(self.texture_path, exist_ok=True)

        # Create pack.mcmeta
        mcmeta = {
            "pack": {
                "pack_format": 15,
                "description": "AI Generated Texture Pack"
            }
        }

        with open(os.path.join(self.base_path, "pack.mcmeta"), "w") as f:
            json.dump(mcmeta, f, indent=4)

    def save_texture(self, image: Image.Image, name: str):
        image.save(os.path.join(self.texture_path, f"{name}.png"))

    def zip_pack(self):
        zip_path = f"{self.pack_name}.zip"

        with zipfile.ZipFile(zip_path, "w") as z:
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, self.base_path)
                    z.write(full_path, relative_path)

        return zip_path