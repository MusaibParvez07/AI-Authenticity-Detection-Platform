from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.config import AUDIO_DIR

from backend.models.user import User

from backend.ai.audio.inference import (
    audio_inference,
)

from backend.ai.audio.model_loader import (
    audio_loader,
)

from backend.services.detection_engine import (
    DetectionEngine,
)

from backend.services.validation_service import (
    validate_extension,
    validate_file_size,
    ALLOWED_AUDIO_EXTENSIONS,
    MAX_AUDIO_SIZE,
)

engine = DetectionEngine(

    inference=audio_inference,

    metadata_loader=audio_loader,

)


async def detect_audio(
    db: Session,
    file: UploadFile,
    current_user: User,
):

    validate_extension(
        file=file,
        allowed_extensions=ALLOWED_AUDIO_EXTENSIONS,
    )

    await validate_file_size(
        file=file,
        max_size=MAX_AUDIO_SIZE,
    )

    return await engine.detect(
        db=db,
        file=file,
        current_user=current_user,
        destination=AUDIO_DIR,
        media_type="audio",
    )