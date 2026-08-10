"""
Video Detection Service

Validates uploaded videos and delegates
processing to the generic DetectionEngine.
"""

from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.config import VIDEO_DIR

from backend.models.user import User

from backend.ai.video.inference import (
    video_inference,
)

from backend.ai.video.model_loader import (
    video_loader,
)

from backend.services.detection_engine import (
    DetectionEngine,
)

from backend.services.validation_service import (
    validate_extension,
    validate_file_size,
    ALLOWED_VIDEO_EXTENSIONS,
    MAX_VIDEO_SIZE,
)

engine = DetectionEngine(

    inference=video_inference,

    metadata_loader=video_loader,

)


async def detect_video(
    db: Session,
    file: UploadFile,
    current_user: User,
):

    validate_extension(
        file=file,
        allowed_extensions=ALLOWED_VIDEO_EXTENSIONS,
    )

    await validate_file_size(
        file=file,
        max_size=MAX_VIDEO_SIZE,
    )

    return await engine.detect(
        db=db,
        file=file,
        current_user=current_user,
        destination=VIDEO_DIR,
        media_type="video",
    )