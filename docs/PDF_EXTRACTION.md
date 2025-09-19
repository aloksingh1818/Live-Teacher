# PDF Extraction Process

## Overview
This document describes the process for extracting text from PDF files in the Live-Teacher backend using PyMuPDF (fitz) and the implemented FastAPI endpoint.

## Extraction Logic
- The function `extract_text_from_pdf(file_path: str) -> List[str]` in `backend/app/pdf.py` uses PyMuPDF to extract text from each page of a PDF file.
- Returns a list of strings, one per page.

## API Endpoint
- **Route:** `POST /upload-pdf/`
- **Description:** Accepts a PDF file upload and returns the extracted text per page as JSON.
- **Request:**
  - Form field: `file` (PDF file)
- **Response:**
  - JSON object: `{ "pages": ["text from page 1", "text from page 2", ...] }`

## Testing
- Use the provided script `backend/test_pdf_extraction.py` to test the endpoint.
- Example:
  ```bash
  python3 backend/test_pdf_extraction.py
  ```
- The script uploads `story.pdf` and prints the extracted text.

## Error Handling
- The endpoint returns HTTP 400 for non-PDF files.
- Returns HTTP 500 for extraction errors (e.g., corrupted PDF).
- All temporary files are cleaned up after processing.

## Sample Output
```
Status Code: 200
Response: {"pages": ["...extracted text..."]}
```