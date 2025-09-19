# Example placeholder for PDF router

import os
import shutil
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from backend.services.pdf_extraction import extract_pdf_text

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...), method: str = "pymupdf"):
    """
    Accepts a PDF file upload, saves it to a temp directory, extracts text, and returns the text.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    temp_dir = "/tmp/live_teacher_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(temp_dir, f"{file_id}.pdf")
    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        text = extract_pdf_text(file_path, method=method)
        if text is None:
            raise HTTPException(status_code=500, detail="Failed to extract text from PDF.")
        return JSONResponse(content={"text": text, "file_id": file_id})
    finally:
        file.file.close()

@router.get("/{pdf_id}/extract")
def extract_text(pdf_id: str):
    return {"message": f"Extract text for PDF {pdf_id}"}
