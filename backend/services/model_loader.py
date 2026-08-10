"""
Model Access Layer

Provides helper functions to retrieve
registered AI models from the global
model registry.
"""

from backend.models.model_metadata import (
    ModelMetadata,
)

from backend.services.model_registry import (
    get_model,
)


# ==========================================================
# Image Model
# ==========================================================

def get_image_model() -> ModelMetadata | None:

    return get_model(
        "image_detector"
    )


# ==========================================================
# Audio Model
# ==========================================================

def get_audio_model() -> ModelMetadata | None:

    return get_model(
        "audio_detector"
    )


# ==========================================================
# Text Model
# ==========================================================

def get_text_model() -> ModelMetadata | None:

    return get_model(
        "text_detector"
    )


# ==========================================================
# Video Model
# ==========================================================

def get_video_model() -> ModelMetadata | None:

    return get_model(
        "video_detector"
    )