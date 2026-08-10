"""
History API

Returns all previous detections
for the authenticated user.
"""

from typing import List

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.models.response_models import (
    HistoryResponse,
)

from backend.models.user import User

from backend.security.auth_dependencies import (
    get_current_user,
)

from backend.services.history_service import (
    get_detection_history,
)

router = APIRouter(
    prefix="/history",
    tags=["History"],
)


@router.get(
    "/",
    response_model=List[HistoryResponse],
    summary="Get Detection History",
)
def history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Returns all previous detections
    belonging to the authenticated user.
    """

    history = get_detection_history(
        db=db,
        user_id=current_user.id,
    )

    return history