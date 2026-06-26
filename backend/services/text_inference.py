import torch

from sqlalchemy.orm import Session

from backend.models.detection_result import DetectionResult

from backend.models.text_models.roberta_detector import (
    TextDetector
)

from backend.services.text_preprocessing import (
    preprocess_text
)


_detector = TextDetector()

_detector.eval()


def detect_text(
    db: Session,
    text: str,
    user_id: int
):

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

    detection = DetectionResult(
        upload_id=None,
        media_type="text",
        input_text=text,
        prediction=label,
        confidence=confidence,
        model_name="AI Text Detector"
    )

    db.add(detection)
    db.commit()
    db.refresh(detection)

    return {
        "status": "success",
        "prediction": label,
        "confidence": confidence,
        "model_name": "AI Text Detector",
        "detection_id": detection.id
    }