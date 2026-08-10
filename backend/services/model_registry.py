"""
Global Model Registry

Stores metadata for every AI model
loaded during application startup.
"""

from backend.models.model_metadata import (
    ModelMetadata,
)

# ==========================================================
# Global Registry
# ==========================================================

MODEL_REGISTRY: dict[str, ModelMetadata] = {}


# ==========================================================
# Register Model
# ==========================================================

def register_model(
    model_name: str,
    metadata: ModelMetadata,
) -> None:

    MODEL_REGISTRY[model_name] = metadata


# ==========================================================
# Get One Model
# ==========================================================

def get_model(
    model_name: str,
) -> ModelMetadata | None:

    return MODEL_REGISTRY.get(model_name)


# ==========================================================
# Get All Models
# ==========================================================

def get_all_models() -> dict[str, ModelMetadata]:

    return MODEL_REGISTRY