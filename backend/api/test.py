from fastapi import APIRouter, UploadFile, File, Depends

from sqlalchemy.orm import Session

from backend.config import IMAGE_DIR

from backend.database.session import get_db

from backend.models.response_models import (
    PredictionResponse
)

from backend.services.file_service import save_file

from backend.services.upload_service import create_upload_record

from backend.services.detection_result_service import (
    save_detection_result
)

from backend.services.inference_service import predict_image

from backend.services.validation_service import (
    validate_extension,
    validate_file_size,
    ALLOWED_IMAGE_EXTENSIONS,
    MAX_IMAGE_SIZE
)

router = APIRouter()


@router.post(
    "/upload-test",
    response_model=PredictionResponse
)
async def upload_test(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
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
        filename=file.filename,
        file_type="image",
        file_path=path
    )

    result = predict_image(
        path
    )

    detection_result = save_detection_result(
        db=db,
        upload_id=upload_record.id,
        prediction=result["prediction"],
        confidence=result["confidence"],
        model_name="ResNet18 DeepFake Detector"
    )

    return PredictionResponse(
        status="success",
        prediction=result["prediction"],
        confidence=result["confidence"],
        file_path=path
    )