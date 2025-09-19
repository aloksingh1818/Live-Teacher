import os
import io
import tempfile
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Helper: create a simple PDF file in memory using PyMuPDF
import fitz

def create_sample_pdf(text="Hello, PDF!"):
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), text)
    pdf_bytes = doc.write()
    doc.close()
    return pdf_bytes

def test_upload_valid_pdf():
    pdf_bytes = create_sample_pdf("Sample PDF text for extraction.")
    files = {"file": ("sample.pdf", io.BytesIO(pdf_bytes), "application/pdf")}
    response = client.post("/pdf/upload", files=files)
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert "Sample PDF text for extraction." in data["text"]

def test_upload_invalid_file():
    files = {"file": ("not_a_pdf.txt", io.BytesIO(b"not a pdf"), "text/plain")}
    response = client.post("/pdf/upload", files=files)
    assert response.status_code == 400
    assert response.json()["detail"] == "Only PDF files are supported."

def test_upload_corrupt_pdf():
    # Corrupt PDF (invalid bytes but with PDF mime type)
    files = {"file": ("corrupt.pdf", io.BytesIO(b"%PDF-1.4\nthis is not a real pdf\n%%EOF"), "application/pdf")}
    response = client.post("/pdf/upload", files=files)
    assert response.status_code == 500
    assert response.json()["detail"] == "Failed to extract text from PDF."
