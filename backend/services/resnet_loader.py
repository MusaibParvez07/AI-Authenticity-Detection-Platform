from backend.models.image_models.resnet_detector import (
    ResNetDetector
)


def load_resnet_model():

    model = ResNetDetector()

    model.eval()

    return model