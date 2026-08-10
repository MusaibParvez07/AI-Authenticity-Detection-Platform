"""
Text Detection Service

Validates uploaded text files and delegates
processing to the generic DetectionEngine.
"""

from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.config import TEXT_DIR

from backend.models.user import User

from backend.ai.text.inference import (
    text_inference,
)

from backend.ai.text.model_loader import (
    text_loader,
)

from backend.services.detection_engine import (
    DetectionEngine,
)

from backend.services.validation_service import (
    validate_extension,
    validate_file_size,
    ALLOWED_TEXT_EXTENSIONS,
    MAX_TEXT_SIZE,
)

engine = DetectionEngine(

    inference=text_inference,

    metadata_loader=text_loader,

)


async def detect_text(
    db: Session,
    file: UploadFile,
    current_user: User,
):

    validate_extension(
        file=file,
        allowed_extensions=ALLOWED_TEXT_EXTENSIONS,
    )

    await validate_file_size(
        file=file,
        max_size=MAX_TEXT_SIZE,
    )

    return await engine.detect(
        db=db,
        file=file,
        current_user=current_user,
        destination=TEXT_DIR,
        media_type="text",
    )