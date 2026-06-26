from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.upload import Upload
from backend.models.detection_result import DetectionResult


def get_dashboard_statistics(
    db: Session,
    user_id: int
):

    total_uploads = (
        db.query(Upload)
        .filter(
            Upload.user_id == user_id
        )
        .count()
    )

    total_predictions = (
        db.query(DetectionResult)
        .join(
            Upload,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id
        )
        .count()
    )

    real_images = (
        db.query(DetectionResult)
        .join(
            Upload,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id,
            DetectionResult.prediction == "real"
        )
        .count()
    )

    fake_images = (
        db.query(DetectionResult)
        .join(
            Upload,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id,
            DetectionResult.prediction == "fake"
        )
        .count()
    )

    image_count = (
        db.query(DetectionResult)
        .join(
            Upload,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id,
            DetectionResult.media_type == "image"
        )
        .count()
    )

    video_count = (
        db.query(DetectionResult)
        .join(
            Upload,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id,
            DetectionResult.media_type == "video"
        )
        .count()
    )

    audio_count = (
        db.query(DetectionResult)
        .join(
            Upload,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id,
            DetectionResult.media_type == "audio"
        )
        .count()
    )

    text_count = (
        db.query(DetectionResult)
        .join(
            Upload,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id,
            DetectionResult.media_type == "text"
        )
        .count()
    )

    average_confidence = (
        db.query(
            func.avg(
                DetectionResult.confidence
            )
        )
        .join(
            Upload,
            Upload.id == DetectionResult.upload_id
        )
        .filter(
            Upload.user_id == user_id
        )
        .scalar()
    )

    latest = (
        db.query(
            Upload.filename,
            Upload.file_type,
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
        .first()
    )

    latest_detection = None

    if latest:

        latest_detection = {
            "filename": latest.filename,
            "file_type": latest.file_type,
            "prediction": latest.prediction,
            "confidence": round(
                latest.confidence,
                4
            ),
            "model_name": latest.model_name,
            "created_at": latest.created_at
        }

    return {
        "total_uploads": total_uploads,
        "total_predictions": total_predictions,
        "real_images": real_images,
        "fake_images": fake_images,
        "image_count": image_count,
        "video_count": video_count,
        "audio_count": audio_count,
        "text_count": text_count,
        "average_confidence": round(
            average_confidence,
            4
        ) if average_confidence else 0,
        "latest_detection": latest_detection
    }