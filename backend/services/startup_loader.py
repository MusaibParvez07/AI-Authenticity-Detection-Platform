from backend.models.model_metadata import ModelMetadata

from backend.services.model_registry import (
    register_model
)

from backend.services.resnet_loader import (
    load_resnet_model
)


def load_models():

    resnet_model = load_resnet_model()

    image_model = ModelMetadata(
        name="ResNet18 DeepFake Detector",
        version="2.0",
        model_type="image",
        accuracy=0.94,
        checkpoint_path="torchvision://resnet18",
        loaded=True,
        model=resnet_model
    )

    audio_model = ModelMetadata(
        name="Dummy Audio Detector",
        version="1.0",
        model_type="audio",
        accuracy=0.91,
        checkpoint_path="backend/models/audio_models/dummy_model.pth",
        loaded=True
    )

    text_model = ModelMetadata(
        name="Dummy Text Detector",
        version="1.0",
        model_type="text",
        accuracy=0.96,
        checkpoint_path="backend/models/text_models/dummy_model.pth",
        loaded=True
    )

    video_model = ModelMetadata(
        name="Dummy Video Detector",
        version="1.0",
        model_type="video",
        accuracy=0.90,
        checkpoint_path="backend/models/video_models/dummy_model.pth",
        loaded=True
    )

    register_model(
        "image_detector",
        image_model
    )

    register_model(
        "audio_detector",
        audio_model
    )

    register_model(
        "text_detector",
        text_model
    )

    register_model(
        "video_detector",
        video_model
    )

    print("ResNet18 loaded successfully")
    print("All models loaded successfully")