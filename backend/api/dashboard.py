from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.security.auth_dependencies import (
    get_current_user
)

from backend.services.dashboard_service import (
    get_dashboard_statistics
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_dashboard_statistics(
        db=db,
        user_id=current_user.id
    )