# Example placeholder for teaching mode router
from fastapi import APIRouter

router = APIRouter()

@router.post("/explain")
def explain():
    return {"message": "Explain endpoint"}
