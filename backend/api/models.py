"""
Models API

Lists every AI model currently loaded
in the application.
"""

from fastapi import APIRouter

from backend.ai.common.model_registry import (
    registry,
)

router = APIRouter(
    prefix="/models",
    tags=["Models"],
)


@router.get("/")
def list_models():

    metadata = registry.get_all_metadata()

    models = []

    for key, info in metadata.items():

        models.append(

            {

                "id": key,

                "name": info.name,

                "version": info.version,

                "media_type": info.media_type,

                "architecture": info.architecture,

                "framework": info.framework,

                "task": info.task,

                "device": info.device,

                "description": info.description,

                "author": info.author,

                "loaded": registry.is_loaded(key),

            }

        )

    return {

        "total_models": registry.total_models(),

        "loaded_models": registry.total_models(),

        "models": models,

    }