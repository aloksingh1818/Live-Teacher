
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
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        text_pages = extract_text_from_pdf(temp_path)
    except Exception as e:
        os.remove(temp_path)
        raise HTTPException(status_code=500, detail=f"PDF extraction failed: {str(e)}")
    os.remove(temp_path)
    return JSONResponse(content={"pages": text_pages})
