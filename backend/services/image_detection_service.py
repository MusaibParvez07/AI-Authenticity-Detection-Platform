from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.config import IMAGE_DIR

from backend.models.user import User

from backend.services.validation_service import (
    validate_extension,
    validate_file_size,
    ALLOWED_IMAGE_EXTENSIONS,
    MAX_IMAGE_SIZE
)

from backend.services.file_service import save_file
from backend.services.upload_service import create_upload_record
from backend.services.inference_service import predict_image
from backend.services.detection_result_service import (
    save_detection_result
)
from backend.services.model_loader import (
    get_image_model
)


async def detect_image(
    db: Session,
    file: UploadFile,
    current_user: User
):

    validate_extension(
        file=file,
        allowed_extensions=ALLOWED_IMAGE_EXTENSIONS
    )

    await validate_file_size(
        file=file,
        max_size=MAX_IMAGE_SIZE
    )

    path = await save_file(
        file=file,
        destination=IMAGE_DIR
    )

    upload_record = create_upload_record(
        db=db,
        user_id=current_user.id,
        filename=file.filename,
        file_type="image",
        file_path=path
    )

    result = predict_image(
        path
    )

    metadata = get_image_model()

    detection = save_detection_result(
        db=db,
        upload_id=upload_record.id,
        prediction=result["prediction"],
        confidence=result["confidence"],
        model_name=metadata.name,
        media_type="image"
    )

    return {
        "status": "success",
        "prediction": result["prediction"],
        "confidence": result["confidence"],
        "file_path": path,
        "upload_id": upload_record.id,
        "detection_id": detection.id
    }