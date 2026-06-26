from backend.models.model_metadata import ModelMetadata

from backend.models.text_models.roberta_detector import (
    RoBERTaDetector
)


def load_roberta():

    model = RoBERTaDetector()

    metadata = ModelMetadata(
        name="RoBERTa Fake News Detector",
        version="1.0.0",
        model_type="text",
        framework="HuggingFace Transformers",
        model=model
    )

    return metadata