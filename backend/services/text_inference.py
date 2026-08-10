import torch

from backend.models.text_models.roberta_detector import (
    TextDetector
)

from backend.services.text_preprocessing import (
    preprocess_text
)


_detector = TextDetector()

_detector.eval()


def predict_text(text: str):

    encoded = preprocess_text(
        text=text
    )

    with torch.no_grad():

        logits = _detector(
            input_ids=encoded["input_ids"],
            attention_mask=encoded["attention_mask"]
        )

        probabilities = torch.softmax(
            logits,
            dim=1
        )

        confidence, prediction = torch.max(
            probabilities,
            dim=1
        )

    label = (
        "real"
        if prediction.item() == 0
        else "fake"
    )

    confidence = round(
        confidence.item(),
        4
    )

    return {
        "prediction": label,
        "confidence": confidence,
        "model_name": "AI Text Detector"
    }