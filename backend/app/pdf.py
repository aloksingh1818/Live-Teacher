# PDF upload and processing routes will go here
import fitz  # PyMuPDF
from typing import List

def extract_text_from_pdf(file_path: str) -> List[str]:
	"""
	Extracts text from each page of a PDF file using PyMuPDF.
	Returns a list of strings, one per page.
	"""
	text_pages = []
	with fitz.open(file_path) as doc:
		for page in doc:
			text_pages.append(page.get_text())
	return text_pages
