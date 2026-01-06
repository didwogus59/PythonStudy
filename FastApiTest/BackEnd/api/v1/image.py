from fastapi import APIRouter, UploadFile, File, HTTPException
from model.response import image_to_response
from service.image_service import process_image

router = APIRouter(tags=["Image"])

@router.post("/image/process")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported image type")

    result = await process_image(file)
    return image_to_response(result)
