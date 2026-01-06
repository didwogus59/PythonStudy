from fastapi import UploadFile
from PIL import Image
import io

async def read_image(file: UploadFile) -> Image.Image:
    contents = await file.read()
    return Image.open(io.BytesIO(contents))

def resize_image(image: Image.Image, width: int, height: int) -> Image.Image:
    return image.resize((width, height))
