from pathlib import Path
from typing import Dict
from typing import Union

from backend.ai.common.inference_engine import (
    InferenceEngine,
)

from backend.ai.image.model_loader import (
    image_loader,
)

from backend.ai.image.preprocessing import (
    preprocess_image,
)


class ImageInference:

    def __init__(self):

        loaded = image_loader.get_model()

        self.model_info = loaded

        self.model = loaded["model"]

        self.processor = loaded["processor"]

        self.device = loaded["device"]

        self.engine = InferenceEngine(

            model=self.model,

            preprocess=lambda image_path: preprocess_image(

                image_path=image_path,

                processor=self.processor,

            ),

        )

    # -------------------------------------------------
    # Convert HuggingFace Labels
    # -------------------------------------------------

    def _normalize_prediction(

        self,

        prediction_index: int,

    ) -> str:

        if hasattr(

            self.model.config,

            "id2label",

        ):

            label = self.model.config.id2label[
                prediction_index
            ].lower()

        else:

            label = str(
                prediction_index
            )

        # AI Labels

        if label in [

            "artificial",

            "ai",

            "generated",

            "synthetic",

            "fake",

        ]:

            return "fake"

        # Human Labels

        if label in [

            "human",

            "real",

            "authentic",

            "natural",

        ]:

            return "real"

        # Unknown

        return label

    # -------------------------------------------------
    # Predict
    # -------------------------------------------------

    def predict(

        self,

        image_path: Union[str, Path],

    ) -> Dict:

        result = self.engine.predict(

            image_path

        )

        prediction_index = result[
            "prediction"
        ]

        prediction = self._normalize_prediction(

            prediction_index

        )

        return {

            "model":

                self.model_info["name"],

            "prediction":

                prediction,

            "prediction_index":

                prediction_index,

            "confidence":

                result["confidence"],

            "confidence_percent":

                result["confidence_percent"],

            "confidence_label":

                result["confidence_label"],

            "device":

                str(self.device),

        }


image_inference = ImageInference()