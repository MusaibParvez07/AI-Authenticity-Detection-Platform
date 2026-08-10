"""
Text Inference

Runs the text detection model through the
shared inference engine.
"""

from backend.ai.common.inference_engine import (
    InferenceEngine,
)

from backend.ai.text.model_loader import (
    text_loader,
)

from backend.ai.text.preprocessing import (
    text_preprocessor,
)


class TextInference:

    def __init__(self):

        self.model = text_loader.load()

        self.engine = InferenceEngine(

            model=self.model,

            preprocess=text_preprocessor.preprocess,

        )

        self.labels = self.model.config.id2label

    # ---------------------------------------
    # Predict
    # ---------------------------------------

    def predict(
        self,
        text: str,
    ):

        result = self.engine.predict(
            text
        )

        label = self.labels[
            result["prediction"]
        ]

        # Normalize output

        if label.lower() == "human":

            prediction = "real"

        elif label.lower() == "chatgpt":

            prediction = "fake"

        else:

            prediction = label.lower()

        confidence = float(
            result["confidence"]
        )

        return {

            "prediction": prediction,

            "confidence": confidence,

            "confidence_percent": round(
                confidence * 100,
                2,
            ),

            "confidence_label":

                "High"

                if confidence >= 0.80

                else

                "Medium"

                if confidence >= 0.60

                else

                "Low",

        }


text_inference = TextInference()