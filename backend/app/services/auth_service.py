from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User
from app.schemas import (
    UserRegister,
    UserLogin
)
from app.utils.password import (
    hash_password,
    verify_password
)
from app.utils.jwt import (
    create_access_token,
    create_refresh_token
)


# REGISTER USER


def register_user(
    user: UserRegister,
    db: Session
):

    # Check username
    existing_username = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Check email
    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Hash password
    hashed_password = hash_password(
        user.password
    )

    # Create user
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )

    # Save user
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



# LOGIN USER


def login_user(
    user: UserLogin,
    db: Session
):

    # Find user
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    password_correct = verify_password(
        user.password,
        existing_user.password_hash
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Create access token
    access_token = create_access_token(
        {
            "sub": str(existing_user.id)
        }
    )

    # Create refresh token
    refresh_token = create_refresh_token(
        {
            "sub": str(existing_user.id)
        }
    )

    # Save refresh token
    existing_user.refresh_token = refresh_token

    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }