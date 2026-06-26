from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.config import AUDIO_DIR

from backend.models.user import User

from backend.services.validation_service import (
    validate_extension,
    validate_file_size,
    ALLOWED_AUDIO_EXTENSIONS,
    MAX_AUDIO_SIZE
)

from backend.services.file_service import save_file

from backend.services.upload_service import create_upload_record

from backend.services.audio_inference import predict_audio

from backend.services.detection_result_service import (
    save_detection_result
)

from backend.services.model_loader import (
    get_audio_model
)


async def detect_audio(
    db: Session,
    file: UploadFile,
    current_user: User
):

    validate_extension(
        file=file,
        allowed_extensions=ALLOWED_AUDIO_EXTENSIONS
    )

    await validate_file_size(
        file=file,
        max_size=MAX_AUDIO_SIZE
    )

    path = await save_file(
        file=file,
        destination=AUDIO_DIR
    )

    upload_record = create_upload_record(
        db=db,
        user_id=current_user.id,
        filename=file.filename,
        file_type="audio",
        file_path=path
    )

    result = predict_audio(
        path
    )

    metadata = get_audio_model()

    detection = save_detection_result(
        db=db,
        upload_id=upload_record.id,
        prediction=result["prediction"],
        confidence=result["confidence"],
        model_name=metadata.name,
        media_type="audio"
    )

    return {
        "status": "success",
        "prediction": result["prediction"],
        "confidence": result["confidence"],
        "file_path": path,
        "upload_id": upload_record.id,
        "detection_id": detection.id
    }