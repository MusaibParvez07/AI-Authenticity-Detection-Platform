from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.upload import Upload
from backend.models.detection_result import DetectionResult

from backend.services.model_registry import (
    get_all_models,
)


def get_dashboard_statistics(
    db: Session,
    user_id: int,
):

    # ----------------------------------------
    # Total Uploads
    # ----------------------------------------

    total_uploads = (
        db.query(Upload)
        .filter(
            Upload.user_id == user_id
        )
        .count()
    )

    # ----------------------------------------
    # Total Predictions
    # ----------------------------------------

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

    # ----------------------------------------
    # Real Predictions
    # ----------------------------------------

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

    # ----------------------------------------
    # Fake Predictions
    # ----------------------------------------

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

    # ----------------------------------------
    # Media Counts
    # ----------------------------------------

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

    # ----------------------------------------
    # Average Confidence
    # ----------------------------------------

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

    # ----------------------------------------
    # Recent Detections
    # ----------------------------------------

    recent = (
        db.query(
            Upload.filename,
            Upload.file_type,
            DetectionResult.media_type,
            DetectionResult.prediction,
            DetectionResult.confidence,
            DetectionResult.model_name,
            DetectionResult.created_at,
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
        .limit(10)
        .all()
    )

    recent_detections = []

    for item in recent:

        recent_detections.append(
            {
                "filename": item.filename,
                "file_type": item.file_type,
                "media_type": item.media_type,
                "prediction": item.prediction,
                "confidence": round(
                    item.confidence,
                    4
                ),
                "model_name": item.model_name,
                "created_at": item.created_at,
            }
        )

    # ----------------------------------------
    # Latest Detection
    # ----------------------------------------

    latest_detection = (
        recent_detections[0]
        if recent_detections
        else None
    )

    # ----------------------------------------
    # System Status
    # ----------------------------------------

    models = get_all_models()

    loaded_models = sum(
    1
    for model in models.values()
    if model.status.lower() == "loaded"
)

    system_status = {
        "backend": "Online",
        "database": "Connected",
        "models_loaded": loaded_models,
        "total_models": len(models),
        "detection_engine": "Running",
        "last_updated": datetime.utcnow().isoformat(),
    }

    # ----------------------------------------
    # Response
    # ----------------------------------------

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
        "latest_detection": latest_detection,
        "recent_detections": recent_detections,
        "system_status": system_status,
    }