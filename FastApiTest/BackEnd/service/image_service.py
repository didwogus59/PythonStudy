from fastapi import UploadFile
from util.image_util import read_image, resize_image

async def process_image(file: UploadFile):
    image = await read_image(file)

    processed = resize_image(image, width=256, height=256)
    
    return processed
