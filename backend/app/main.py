from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.services.startup_loader import load_models

from backend.api.models import router as models_router
from backend.api.history import router as history_router
from backend.api.dashboard import router as dashboard_router
from backend.api.image import router as image_router
from backend.api.audio import router as audio_router
from backend.api.video import router as video_router
from backend.api.text import router as text_router
from backend.api.test import router as test_router
from backend.api.auth import router as auth_router


app = FastAPI(
    title="Multi-Modal AI Fake Detection System",
    version="1.0.0",
    description="AI-powered system for detecting fake images, videos, audio, and text."
)

# ----------------------------------------------------
# CORS Configuration
# ----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://192.168.1.36:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
# Startup
# ----------------------------------------------------

@app.on_event("startup")
async def startup_event():
    load_models()


@app.get("/")
def home():
    return {
        "message": "Fake Detection System Backend Running"
    }


app.include_router(models_router)
app.include_router(history_router)
app.include_router(dashboard_router)
app.include_router(image_router)
app.include_router(audio_router)
app.include_router(video_router)
app.include_router(text_router)
app.include_router(test_router)
app.include_router(auth_router)