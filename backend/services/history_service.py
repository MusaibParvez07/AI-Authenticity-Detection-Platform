from sqlalchemy.orm import Session

from backend.models.upload import Upload
from backend.models.detection_result import DetectionResult


def get_detection_history(
    db: Session,
    user_id: int
):

    results = (
        db.query(
            Upload.id.label("upload_id"),
            Upload.filename,
            Upload.file_type,
            DetectionResult.id.label("detection_id"),
            DetectionResult.media_type,
            DetectionResult.prediction,
            DetectionResult.confidence,
            DetectionResult.model_name,
            DetectionResult.created_at
        )
        .join(
            DetectionResult,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id
        )
        .order_by(
            DetectionResult.created_at.desc()
        )
        .all()
    )

    history = []

    for result in results:

        history.append(
            {
                "upload_id": result.upload_id,
                "detection_id": result.detection_id,
                "filename": result.filename,
                "file_type": result.file_type,
                "media_type": result.media_type,
                "prediction": result.prediction,
                "confidence": result.confidence,
                "model_name": result.model_name,
                "created_at": result.created_at
            }
        )

    return history