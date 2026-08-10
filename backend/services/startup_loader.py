"""
Application Startup Loader

Loads and registers all AI models during
FastAPI startup.
"""

from backend.ai.image.model_loader import image_loader
from backend.ai.audio.model_loader import audio_loader
from backend.ai.video.model_loader import video_loader
from backend.ai.text.model_loader import text_loader

from backend.services.model_registry import (
    register_model,
)


def load_models():

    print("=" * 60)
    print("Loading AI Models...")
    print("=" * 60)

    # =====================================================
    # IMAGE
    # =====================================================

    image_loader.load()

    register_model(
        model_name="image_detector",
        metadata=image_loader.get_metadata(),
    )

    print("✅ Image Model Loaded")

    # =====================================================
    # AUDIO
    # =====================================================

    audio_loader.load()

    register_model(
        model_name="audio_detector",
        metadata=audio_loader.get_metadata(),
    )

    print("✅ Audio Model Loaded")

    # =====================================================
    # VIDEO
    # =====================================================

    video_loader.load()

    register_model(
        model_name="video_detector",
        metadata=video_loader.get_metadata(),
    )

    print("✅ Video Model Loaded")

    # =====================================================
    # TEXT
    # =====================================================

    text_loader.load()

    register_model(
        model_name="text_detector",
        metadata=text_loader.get_metadata(),
    )

    print("✅ Text Model Loaded")

    print("=" * 60)
    print("Startup Completed Successfully")
    print("=" * 60)