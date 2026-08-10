"""
Video Model Loader

Loads the primary video detection model
and exposes metadata.
"""

import torch

from torchvision.models import (
    ResNet18_Weights,
    resnet18,
)

from backend.ai.common.device import DEVICE
from backend.ai.common.metadata import ModelMetadata


class VideoModelLoader:

    def __init__(self):

        self.model = None
        self.metadata = None

    # -------------------------------------------------

    def load(self):

        if self.model is not None:
            return self.model

        self.model = resnet18(
            weights=ResNet18_Weights.DEFAULT
        )

        self.model.fc = torch.nn.Linear(
            self.model.fc.in_features,
            2,
        )

        self.model.to(DEVICE)

        self.model.eval()

        self.metadata = ModelMetadata(

            name="Video Detector",

            version="1.0.0",

            media_type="video",

            architecture="ResNet18",

            framework="PyTorch",

            task="AI Video Detection",

            dataset="ImageNet",

            input_size="224 x 224",

            classes=[
                "real",
                "fake",
            ],

            confidence_threshold=0.50,

            weights_path="TorchVision",

            device=str(DEVICE),

            description="Frame-based AI Video Detector",

            author="Mukund",

            status="loaded",

        )

        return self.model

    # -------------------------------------------------

    def get_metadata(self):

        if self.metadata is None:

            self.load()

        return self.metadata


video_loader = VideoModelLoader()