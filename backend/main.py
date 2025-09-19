from fastapi import FastAPI
from routers import auth, pdf, tts, progress, teach

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(pdf.router, prefix="/pdf", tags=["pdf"])
app.include_router(tts.router, prefix="/tts", tags=["tts"])
app.include_router(progress.router, prefix="/progress", tags=["progress"])
app.include_router(teach.router, prefix="/teach", tags=["teach"])

@app.get("/")
def root():
    return {"message": "Live-Teacher FastAPI backend is running."}
