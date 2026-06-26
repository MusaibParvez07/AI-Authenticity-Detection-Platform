from sqlalchemy.orm import Session

from backend.security.hashing import (
    hash_password,
    verify_password
)

from backend.security.jwt_handler import (
    create_access_token
)

from backend.services.user_service import (
    get_user_by_email,
    create_user
)


def register_user(
    db: Session,
    name: str,
    email: str,
    password: str
):

    existing = get_user_by_email(
        db,
        email
    )

    if existing:

        raise Exception(
            "Email already registered."
        )

    hashed = hash_password(
        password
    )

    return create_user(
        db,
        name,
        email,
        hashed
    )


def login_user(
    db: Session,
    email: str,
    password: str
):

    user = get_user_by_email(
        db,
        email
    )

    if user is None:

        raise Exception(
            "Invalid credentials."
        )

    if not verify_password(
        password,
        user.password_hash
    ):

        raise Exception(
            "Invalid credentials."
        )

    token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id,
            "name": user.name
        }
    )

    return token