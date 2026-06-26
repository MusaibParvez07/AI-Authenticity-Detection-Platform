from fastapi import APIRouter

from backend.services.model_registry import (
    get_all_models
)

router = APIRouter()


@router.get("/models")
def list_models():

    models = get_all_models()

    response = {}

    for key, model in models.items():

        response[key] = {
            "name": model.name,
            "version": model.version,
            "model_type": model.model_type,
            "accuracy": model.accuracy,
            "checkpoint_path": model.checkpoint_path,
            "loaded": model.loaded
        }

    return response