"""
Text Model Loader

Loads the AI Text Detection model.
"""

from transformers import AutoModelForSequenceClassification

from backend.ai.common.device import DEVICE
from backend.ai.common.metadata import ModelMetadata

from backend.ai.config import (
    TEXT_MODEL_NAME,
    TEXT_MAX_LENGTH,
)


class TextModelLoader:

    def __init__(self):

        self.model = None

        self.metadata = None

    # ----------------------------------
    # Load Model
    # ----------------------------------

    def load(self):

        if self.model is not None:

            return self.model

        print("=" * 60)
        print("TEXT MODEL LOADER")
        print("=" * 60)
        print(f"Loading Model : {TEXT_MODEL_NAME}")
        print()

        self.model = AutoModelForSequenceClassification.from_pretrained(
            TEXT_MODEL_NAME
        )

        self.model.to(DEVICE)

        self.model.eval()

        print("=" * 60)
        print("TEXT MODEL INFORMATION")
        print("=" * 60)

        print(f"Model      : {TEXT_MODEL_NAME}")
        print(f"Device     : {DEVICE}")

        if hasattr(self.model.config, "_name_or_path"):

            print(
                f"Checkpoint : {self.model.config._name_or_path}"
            )

        if hasattr(self.model.config, "id2label"):

            print(
                f"ID2LABEL   : {self.model.config.id2label}"
            )

        if hasattr(self.model.config, "label2id"):

            print(
                f"LABEL2ID   : {self.model.config.label2id}"
            )

        print("=" * 60)

        architecture = getattr(

            self.model.config,

            "model_type",

            "Transformer",

        )

        classes = []

        if hasattr(self.model.config, "id2label"):

            classes = list(
                self.model.config.id2label.values()
            )

        self.metadata = ModelMetadata(

            name="Text Detector",

            version="2.0.0",

            media_type="text",

            architecture=architecture,

            framework="Transformers",

            task="AI Text Detection",

            dataset="Pretrained HuggingFace",

            input_size=f"{TEXT_MAX_LENGTH} tokens",

            classes=classes,

            confidence_threshold=0.50,

            weights_path="HuggingFace",

            device=str(DEVICE),

            description="Fine-tuned AI Text Detection Model",

            author="Mukund",

            status="loaded",

        )

        print("✅ Text Model Loaded Successfully")
        print("=" * 60)

        return self.model

    # ----------------------------------
    # Metadata
    # ----------------------------------

    def get_metadata(self):

        if self.metadata is None:

            self.load()

        return self.metadata


text_loader = TextModelLoader()