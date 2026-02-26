from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from generator import TextureGenerator
from pack_builder import PackBuilder
import uvicorn

app = FastAPI()

generator = TextureGenerator()

@app.post("/generate")
async def generate(
    block_name: str = Form(...),
    resolution: int = Form(...),
    style: str = Form(...)
):

    pack = PackBuilder("AI_Texture_Pack")
    pack.create_structure()

    image = generator.generate_texture(block_name, resolution, style)

    pack.save_texture(image, block_name)

    zip_file = pack.zip_pack()

    return FileResponse(zip_file, media_type='application/zip', filename=zip_file)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)