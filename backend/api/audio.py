"""
Audio Detection API

Handles authenticated audio uploads and
delegates processing to the audio detection service.
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

from backend.services.audio_detection_service import (
    detect_audio,
)

router = APIRouter(
    prefix="/detect",
    tags=["Audio Detection"],
)


@router.post(
    "/audio",
    response_model=PredictionResponse,
    summary="Analyze an uploaded audio file",
)
async def detect_audio_api(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    result = await detect_audio(
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