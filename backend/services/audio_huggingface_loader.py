from transformers import AutoProcessor
from transformers import AutoModelForAudioClassification


MODEL_NAME = "superb/wav2vec2-base-superb-ks"


def load_audio_model():

    processor = AutoProcessor.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForAudioClassification.from_pretrained(
        MODEL_NAME
    )

    model.eval()

    return processor, model