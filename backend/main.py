
# Entry point for FastAPI backend
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
from app.pdf import extract_text_from_pdf

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Live-Teacher Backend Running"}


# PDF upload and extraction endpoint
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file and extract its text using PyMuPDF.
    Returns the extracted text per page.
    """
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, file.filename)
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save uploaded file: {str(e)}")
    try:
        text_pages = extract_text_from_pdf(temp_path)
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise HTTPException(status_code=500, detail=f"PDF extraction failed: {str(e)}")
    if os.path.exists(temp_path):
        os.remove(temp_path)
    if not text_pages or all(not page.strip() for page in text_pages):
        raise HTTPException(status_code=422, detail="No extractable text found in PDF.")
    return JSONResponse(content={"pages": text_pages})
