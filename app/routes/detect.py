from fastapi import APIRouter
from app.schemas.request import DetectRequest
from app.services.detection import detect_language

router = APIRouter()

@router.post("/detect")
async def detect_lang(request: DetectRequest):
    """
    API endpoint for detecting the language of a given text.
    """
    language = detect_language(request.text)
    return {"language": language}
