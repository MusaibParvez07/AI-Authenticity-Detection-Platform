from transformers import AutoModelForAudioClassification

from backend.ai.common.device import DEVICE
from backend.ai.common.metadata import ModelMetadata

from backend.ai.config import (
    AUDIO_MODEL_NAME,
    AUDIO_NUM_CLASSES,
    AUDIO_MAX_DURATION,
)


class AudioModelLoader:

    def __init__(self):

        self.model = None
        self.metadata = None

    def load(self):

        if self.model is not None:
            return self.model

        self.model = AutoModelForAudioClassification.from_pretrained(
            AUDIO_MODEL_NAME,
            num_labels=AUDIO_NUM_CLASSES,
            ignore_mismatched_sizes=True,
        )

        self.model.to(DEVICE)
        self.model.eval()

        self.metadata = ModelMetadata(

            name="Audio Detector",

            version="1.0.0",

            media_type="audio",

            architecture="Wav2Vec2",

            framework="Transformers",

            task="AI Audio Detection",

            dataset="Pretrained",

            input_size=f"{AUDIO_MAX_DURATION} sec",

            classes=["real", "fake"],

            confidence_threshold=0.5,

            weights_path="HuggingFace",

            device=str(DEVICE),

            description="Wav2Vec2 pretrained classifier",

            author="Mukund",

            status="loaded",

        )

        return self.model

    def get_metadata(self):

        if self.metadata is None:
            self.load()

        return self.metadata


audio_loader = AudioModelLoader()