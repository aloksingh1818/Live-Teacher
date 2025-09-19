# PDF Extraction Process (Backend)

This document describes the PDF text extraction process for the Live-Teacher backend.

## Overview
- The backend provides a `/pdf/upload` endpoint for uploading PDF files.
- Uploaded PDFs are saved to a temporary directory on the server.
- Text extraction is performed using either PyMuPDF or pdfminer.six (configurable).
- The extracted text is returned in the API response.

## Steps
1. **Upload**: Client sends a POST request to `/pdf/upload` with a PDF file (multipart/form-data).
2. **Validation**: The backend checks the file type (must be `application/pdf`).
3. **Save**: The file is saved to `/tmp/live_teacher_uploads/<uuid>.pdf`.
4. **Extraction**: The backend calls `extract_pdf_text()` from `backend/services/pdf_extraction.py`:
    - Default method: PyMuPDF (fast, good for most PDFs)
    - Alternative: pdfminer.six (for complex PDFs)
5. **Error Handling**:
    - If the file is not a PDF, returns 400 error.
    - If extraction fails, returns 500 error.
6. **Response**: On success, returns `{ "text": <extracted_text>, "file_id": <uuid> }`.

## Example Usage
```
curl -X POST -F "file=@story.pdf" http://localhost:8000/pdf/upload
```

## Code Reference
- Endpoint: `backend/routers/pdf.py`
- Extraction logic: `backend/services/pdf_extraction.py`
- Tests: `backend/tests/test_pdf_extraction.py`

## Notes
- Both extraction libraries are installed; method can be selected via the `method` query param.
- Temporary files are not deleted automatically (for demo/testing).
- For production, add cleanup and security checks.
