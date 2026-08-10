"""
Model Status Service

Returns the current status of every
AI model loaded by the backend.
"""

from backend.ai.image.model_loader import image_loader
from backend.ai.audio.model_loader import audio_loader
from backend.ai.video.model_loader import video_loader
from backend.ai.text.model_loader import text_loader


def get_models_status():

    image = image_loader.get_metadata()
    audio = audio_loader.get_metadata()
    video = video_loader.get_metadata()
    text = text_loader.get_metadata()

    return {

        "total_models": 4,

        "loaded_models": 4,

        "models": [

            {
                "name": image.name,
                "type": "Image",
                "status": "Loaded",
                "device": image.device,
                "version": image.version,
            },

            {
                "name": audio.name,
                "type": "Audio",
                "status": "Loaded",
                "device": audio.device,
                "version": audio.version,
            },

            {
                "name": text.name,
                "type": "Text",
                "status": "Loaded",
                "device": text.device,
                "version": text.version,
            },

            {
                "name": video.name,
                "type": "Video",
                "status": "Loaded",
                "device": video.device,
                "version": video.version,
            },

        ],

    }