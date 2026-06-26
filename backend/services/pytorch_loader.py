import torch

from backend.models.image_models.deepfake_detector import (
    DeepFakeDetector
)


def load_deepfake_model():

    model = DeepFakeDetector()

    model.eval()

    return model