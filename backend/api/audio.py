from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import File

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.security.auth_dependencies import (
    get_current_user
)

from backend.services.audio_detection_service import (
    detect_audio
)

router = APIRouter(
    prefix="/detect",
    tags=["Audio Detection"]
)


@router.post("/audio")
async def detect_audio_api(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return await detect_audio(
        db=db,
        file=file,
        current_user=current_user
    )