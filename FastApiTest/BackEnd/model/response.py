from fastapi.responses import StreamingResponse
import io

def image_to_response(image):
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")