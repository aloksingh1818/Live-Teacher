"""
PDF text extraction service using PyMuPDF and pdfminer.six.
"""
import fitz  # PyMuPDF
from pdfminer.high_level import extract_text as pdfminer_extract_text
from typing import Optional


def extract_text_pymupdf(pdf_path: str) -> Optional[str]:
    """
    Extract all text from a PDF file using PyMuPDF.
    Returns the extracted text or None if extraction fails.
    """
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join(page.get_text() for page in doc)
        doc.close()
        return text
    except Exception as e:
        print(f"PyMuPDF extraction error: {e}")
        return None


def extract_text_pdfminer(pdf_path: str) -> Optional[str]:
    """
    Extract all text from a PDF file using pdfminer.six.
    Returns the extracted text or None if extraction fails.
    """
    try:
        text = pdfminer_extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"pdfminer.six extraction error: {e}")
        return None


def extract_pdf_text(pdf_path: str, method: str = "pymupdf") -> Optional[str]:
    """
    Extract text from a PDF file using the specified method ('pymupdf' or 'pdfminer').
    Returns the extracted text or None if extraction fails.
    """
    if method == "pymupdf":
        return extract_text_pymupdf(pdf_path)
    elif method == "pdfminer":
        return extract_text_pdfminer(pdf_path)
    else:
        raise ValueError("Invalid extraction method. Use 'pymupdf' or 'pdfminer'.")
