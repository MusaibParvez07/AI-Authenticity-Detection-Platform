"""
Image Detection Service

Validates uploaded images and runs the
complete image forensic pipeline.
"""

from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.config import IMAGE_DIR

from backend.models.user import User

from backend.ai.image.inference import (
    image_inference,
)

from backend.ai.image.model_loader import (
    image_loader,
)

from backend.ai.image.pipeline import (
    image_pipeline,
)

from backend.services.detection_engine import (
    DetectionEngine,
)

from backend.services.validation_service import (
    validate_extension,
    validate_file_size,
    ALLOWED_IMAGE_EXTENSIONS,
    MAX_IMAGE_SIZE,
)


# ==========================================================
# Detection Engine
# ==========================================================

engine = DetectionEngine(

    inference=image_inference,

    metadata_loader=image_loader,

    pipeline=image_pipeline,

)


# ==========================================================
# Image Detection
# ==========================================================

async def detect_image(
    db: Session,
    file: UploadFile,
    current_user: User,
):

    # --------------------------------------------------
    # Validate File Extension
    # --------------------------------------------------

    validate_extension(

        file=file,

        allowed_extensions=ALLOWED_IMAGE_EXTENSIONS,

    )

    # --------------------------------------------------
    # Validate File Size
    # --------------------------------------------------

    await validate_file_size(

        file=file,

        max_size=MAX_IMAGE_SIZE,

    )

    # --------------------------------------------------
    # Run Detection Engine
    # --------------------------------------------------

    return await engine.detect(

        db=db,

        file=file,

        current_user=current_user,

        destination=IMAGE_DIR,

        media_type="image",

    )