"""
Audio Inference

Runs the audio detection model through the
shared inference engine.
"""

from backend.ai.audio.model_loader import (
    audio_loader,
)

from backend.ai.audio.preprocessing import (
    audio_preprocessor,
)

from backend.ai.common.inference_engine import (
    InferenceEngine,
)

from backend.ai.config import (
    AUDIO_CLASSES,
)


class AudioInference:

    def __init__(self):

        model = audio_loader.load()

        self.engine = InferenceEngine(

            model=model,

            preprocess=audio_preprocessor.preprocess,

        )

        self.classes = AUDIO_CLASSES

    # ---------------------------------------
    # Predict
    # ---------------------------------------

    def predict(
        self,
        audio_path: str,
    ):

        result = self.engine.predict(
            audio_path
        )

        prediction = self.classes[
            result["prediction"]
        ]

        confidence = float(
            result["confidence"]
        )

        return {

            "prediction":
                prediction,

            "confidence":
                confidence,

            "confidence_percent":
                round(
                    confidence * 100,
                    2
                ),

            "confidence_label":

                "High"

                if confidence >= 0.80

                else

                "Medium"

                if confidence >= 0.60

                else

                "Low",

            "device":
                result.get(
                    "device"
                ),

        }


audio_inference = AudioInference()