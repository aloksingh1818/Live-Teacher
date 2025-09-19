# Example placeholder for TTS router
from fastapi import APIRouter

router = APIRouter()

@router.post("/speak")
def tts_speak():
    return {"message": "TTS speak endpoint"}
