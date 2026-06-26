from typing import Optional

from sqlalchemy.orm import Session

from backend.models.detection_result import DetectionResult


def save_detection_result(
    db: Session,
    prediction: str,
    confidence: float,
    model_name: str,
    media_type: str,
    upload_id: Optional[int] = None,
    input_text: Optional[str] = None
) -> DetectionResult:

    detection = DetectionResult(
        upload_id=upload_id,
        media_type=media_type,
        input_text=input_text,
        prediction=prediction,
        confidence=confidence,
        model_name=model_name
    )

    db.add(detection)

    db.commit()

    db.refresh(detection)

    return detection