from backend.models.model_metadata import ModelMetadata


MODEL_REGISTRY = {}


def register_model(
    model_name: str,
    metadata: ModelMetadata
):

    MODEL_REGISTRY[model_name] = metadata


def get_model(
    model_name: str
):

    return MODEL_REGISTRY.get(model_name)


def get_all_models():

    return MODEL_REGISTRY