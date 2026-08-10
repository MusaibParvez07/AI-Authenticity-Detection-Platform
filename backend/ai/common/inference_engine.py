from typing import Any
from typing import Callable

import torch

from backend.ai.common.confidence import (
    confidence_label,
    confidence_percentage,
)

from backend.ai.common.device import DEVICE


class InferenceEngine:

    def __init__(
        self,
        model: Any,
        preprocess: Callable,
    ):

        self.model = model

        if hasattr(self.model, "to"):
            self.model = self.model.to(DEVICE)

        if hasattr(self.model, "eval"):
            self.model.eval()

        self.preprocess = preprocess

    # --------------------------------------------------
    # Move Inputs To Device
    # --------------------------------------------------

    def _move_to_device(
        self,
        data: Any,
    ):

        if hasattr(data, "items"):

            moved = {}

            for key, value in data.items():

                if hasattr(value, "to"):

                    moved[key] = value.to(DEVICE)

                else:

                    moved[key] = value

            return moved

        if hasattr(data, "to"):

            return data.to(DEVICE)

        return data

    # --------------------------------------------------
    # Forward Pass
    # --------------------------------------------------

    def _forward(
        self,
        processed: Any,
    ):

        with torch.inference_mode():

            if hasattr(processed, "items"):

                outputs = self.model(**processed)

            else:

                outputs = self.model(processed)

        if hasattr(outputs, "logits"):

            return outputs.logits

        return outputs

    # --------------------------------------------------
    # Predict
    # --------------------------------------------------

    def predict(
        self,
        input_data: Any,
    ):

        processed = self.preprocess(
            input_data
        )

        processed = self._move_to_device(
            processed
        )

        logits = self._forward(
            processed
        )

        probabilities = torch.softmax(
            logits,
            dim=1,
        )

        prediction = torch.argmax(
            probabilities,
            dim=1,
        ).item()

        confidence = probabilities[
            0,
            prediction
        ].item()

        # ------------------------------------------
        # Optional Debug
        # ------------------------------------------

        DEBUG = False

        if DEBUG:

            print(
                f"[Inference] "
                f"Prediction={prediction} "
                f"Confidence={confidence:.4f}"
            )

        return {

            "prediction": prediction,

            "confidence": confidence,

            "confidence_percent":
                confidence_percentage(
                    confidence
                ),

            "confidence_label":
                confidence_label(
                    confidence
                ),

            "device": str(
                DEVICE
            ),

        }