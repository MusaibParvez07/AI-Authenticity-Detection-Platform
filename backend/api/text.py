from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.models.request_models import (
    TextRequest
)

from backend.security.auth_dependencies import (
    get_current_user
)

from backend.services.text_inference import (
    detect_text
)

router = APIRouter(
    prefix="/detect",
    tags=["Text Detection"]
)


@router.post("/text")
def detect_text_api(
    request: TextRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return detect_text(
        db=db,
        text=request.text,
        user_id=current_user.id
    )