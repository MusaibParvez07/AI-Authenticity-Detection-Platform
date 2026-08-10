"""
Video Detection API

Handles authenticated video uploads and
delegates processing to the video detection service.
"""

from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
)

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.models.response_models import PredictionResponse

from backend.models.user import User

from backend.security.auth_dependencies import (
    get_current_user,
)

from backend.services.video_detection_service import (
    detect_video,
)

router = APIRouter(
    prefix="/detect",
    tags=["Video Detection"],
)


@router.post(
    "/video",
    response_model=PredictionResponse,
    summary="Analyze an uploaded video",
)
async def video_detection(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    result = await detect_video(
        db=db,
        file=file,
        current_user=current_user,
    )

    return PredictionResponse(
        status=result["status"],
        prediction=result["prediction"],
        confidence=result["confidence"],
        file_path=result["file_path"],
        upload_id=result["upload_id"],
        detection_id=result["detection_id"],
    )