from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.security.auth_dependencies import (
    get_current_user
)

from backend.services.history_service import (
    get_detection_history
)

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def history(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_detection_history(
        db=db,
        user_id=current_user.id
    )