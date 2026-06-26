from backend.services.model_registry import (
    get_model
)


def get_image_model():

    return get_model(
        "image_detector"
    )


def get_audio_model():

    return get_model(
        "audio_detector"
    )


def get_text_model():

    return get_model(
        "text_detector"
    )


def get_video_model():

    return get_model(
        "video_detector"
    )