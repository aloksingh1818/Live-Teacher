import requests

# Replace with the actual path to your sample PDF file
PDF_PATH = "story.pdf"
API_URL = "http://localhost:8000/upload-pdf/"

with open(PDF_PATH, "rb") as f:
    files = {"file": (PDF_PATH, f, "application/pdf")}
    response = requests.post(API_URL, files=files)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
