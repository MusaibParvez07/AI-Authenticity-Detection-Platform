from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.models.auth_models import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)

from backend.services.auth_service import (
    register_user,
    login_user
)

from backend.security.auth_dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    try:

        register_user(
            db=db,
            name=request.name,
            email=request.email,
            password=request.password
        )

        return {
            "status": "success",
            "message": "User registered successfully."
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    try:

        token = login_user(
            db=db,
            email=request.email,
            password=request.password
        )

        return TokenResponse(
            access_token=token
        )

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )


@router.get("/me")
def me(
    user=Depends(get_current_user)
):

    return {
        "logged_in_user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }