
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# CORS middleware must be added before routers or anything else
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bug-free-sniffle-v6vv59q6675pcwq79-5173.app.github.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from backend.routers import auth, pdf, tts, progress, teach
print("Including routers: auth, pdf, tts, progress, teach")
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(pdf.router, prefix="/pdf", tags=["pdf"])
app.include_router(tts.router, prefix="/tts", tags=["tts"])
app.include_router(progress.router, prefix="/progress", tags=["progress"])
app.include_router(teach.router, prefix="/teach", tags=["teach"])

@app.get("/")
def root():
    return {"message": "Live-Teacher FastAPI backend is running."}
