"""
Image Detection API

Authenticated endpoint for complete
AI forensic image analysis.
"""

from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
)

from sqlalchemy.orm import Session

from backend.database.session import (
    get_db,
)

from backend.models.user import User

from backend.models.response_models import (
    ImagePredictionResponse,
)

from backend.security.auth_dependencies import (
    get_current_user,
)

from backend.services.image_detection_service import (
    detect_image,
)

router = APIRouter(
    prefix="/detect",
    tags=["Image Detection"],
)


@router.post(
    "/image",
    response_model=ImagePredictionResponse,
    summary="Complete Image Forensic Analysis",
)
async def image_detection(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Upload an image and run the complete
    AI forensic pipeline.
    """

    result = await detect_image(
        db=db,
        file=file,
        current_user=current_user,
    )

    return ImagePredictionResponse(

        status=result["status"],

        prediction=result["prediction"],

        confidence=result["confidence"],

        file_path=result["file_path"],

        upload_id=result["upload_id"],

        detection_id=result["detection_id"],

        report=result["report"],

    )