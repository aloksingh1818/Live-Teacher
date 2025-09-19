---
# PDF Extraction Process (Live-Teacher Backend)

This document describes how PDF text extraction is implemented and handled in the Live-Teacher backend.

## Overview
The backend provides an endpoint `/upload-pdf/` that allows users to upload a PDF file. The server extracts text from each page using PyMuPDF and returns the result as a JSON response.

## Extraction Flow
1. **Upload**: User sends a POST request to `/upload-pdf/` with a PDF file as form data (`file`).
2. **Save**: The server saves the uploaded file to a temporary directory.
3. **Extract**: The server uses PyMuPDF (`fitz`) to extract text from each page.
4. **Cleanup**: The temporary file is deleted after extraction (or on error).
5. **Response**: The server returns a JSON object with a list of text strings (one per page).

## Error Handling
- Only files with a `.pdf` extension are accepted.
- If the file cannot be saved, a 500 error is returned.
- If extraction fails (corrupt, encrypted, or invalid PDF), a 500 error is returned.
- If no extractable text is found, a 422 error is returned.
- All errors include a clear message in the response.

## Example Request (curl)
```
curl -X POST "http://localhost:8000/upload-pdf/" -F "file=@/path/to/your.pdf"
```

## Example Response
```
{
  "pages": [
    "Text from page 1...",
    "Text from page 2..."
  ]
}
```

## Dependencies
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [FastAPI](https://fastapi.tiangolo.com/)

---