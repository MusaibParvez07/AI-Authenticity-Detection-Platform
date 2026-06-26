from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.security.jwt_handler import decode_access_token
from backend.services.user_service import get_user_by_email


security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Authentication required."
        )

    print("\n========== AUTH DEBUG ==========")
    print("Credentials:", credentials)

    payload = decode_access_token(credentials.credentials)

    print("Decoded Payload:", payload)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token."
        )

    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token."
        )

    user = get_user_by_email(
        db=db,
        email=email
    )

    print("Database User:", user)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found."
        )

    print("========== AUTH SUCCESS ==========\n")

    return user