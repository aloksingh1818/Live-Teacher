# Entry point for FastAPI backend
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Live-Teacher Backend Running"}
