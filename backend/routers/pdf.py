# Example placeholder for PDF router
from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
def upload_pdf():
    return {"message": "PDF upload endpoint"}

@router.get("/{pdf_id}/extract")
def extract_text(pdf_id: str):
    return {"message": f"Extract text for PDF {pdf_id}"}
