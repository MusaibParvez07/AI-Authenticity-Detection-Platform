"""
Image Model Loader

Loads the primary AI image detection model
and registers it into the global registry.
"""

import logging

from backend.ai.common.metadata import ModelMetadata
from backend.ai.common.model_registry import registry

from backend.ai.image.loaders.image_detector_loader import (
    load_siglip_model,
)

logger = logging.getLogger(__name__)


class ImageModelLoader:

    def __init__(self):

        self.models = {}

        self.metadata = {}

    # -------------------------------------------------
    # Load Primary Detector
    # -------------------------------------------------

    def load(self):

        if self.models:

            return self.models

        print("=" * 60)
        print("IMAGE MODEL LOADER")
        print("=" * 60)

        detector = load_siglip_model()

        model = detector["model"]

        processor = detector["processor"]

        device = detector["device"]

        model_name = detector["name"]

        print(f"Loaded Model : {model_name}")

        if hasattr(model.config, "_name_or_path"):
            print(f"Checkpoint   : {model.config._name_or_path}")

        if hasattr(model.config, "id2label"):
            print(f"Labels       : {model.config.id2label}")

        self.models = {

            "primary": {

                "name": model_name,

                "model": model,

                "processor": processor,

                "device": device,

            }

        }

        # ---------------------------------------------
        # Metadata
        # ---------------------------------------------

        labels = []

        if hasattr(model.config, "id2label"):

            labels = list(
                model.config.id2label.values()
            )

        metadata = ModelMetadata(

            name=model_name,

            version="1.0.0",

            media_type="image",

            architecture=model.__class__.__name__,

            framework="Transformers",

            task="AI Image Detection",

            dataset="HuggingFace",

            input_size="Auto",

            classes=labels,

            confidence_threshold=0.50,

            weights_path="backend/weights/image",

            device=str(device),

            description="Primary AI Image Detector",

            author="Mukund",

        )

        registry.register(

            name="primary_image_detector",

            model=model,

            metadata=metadata,

        )

        self.metadata["primary"] = metadata

        print("✅ Primary Image Detector Registered")

        print("=" * 60)

        return self.models

    # -------------------------------------------------

    def get_models(self):

        if not self.models:

            self.load()

        return self.models

    # -------------------------------------------------

    def get_model(self):

        return self.get_models()["primary"]

    # -------------------------------------------------

    def get_metadata(self):

        if not self.metadata:

            self.load()

        return self.metadata["primary"]

    # -------------------------------------------------

    def get_registry_model(self):

        return registry.get(

            "primary_image_detector"

        )

    # -------------------------------------------------

    def get_registry_metadata(self):

        return registry.get_metadata(

            "primary_image_detector"

        )


image_loader = ImageModelLoader()