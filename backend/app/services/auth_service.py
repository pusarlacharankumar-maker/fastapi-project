from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User

from app.schemas import (
    UserRegister,
    UserLogin,
    UserProfileUpdate,
    ChangePassword
)

from app.utils.password import (
    hash_password,
    verify_password
)

from app.utils.jwt import (
    create_access_token,
    create_refresh_token,
    verify_refresh_token
)


# =========================
# REGISTER USER
# =========================

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

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# =========================
# LOGIN USER
# =========================

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
        existing_user.id
    )

    # Create refresh token
    refresh_token = create_refresh_token(
        existing_user.id
    )

    # Save refresh token
    existing_user.refresh_token = refresh_token

    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# =========================
# LOGOUT USER
# =========================

def logout_user(
    current_user: User,
    db: Session
):
    # Remove refresh token
    current_user.refresh_token = None

    db.commit()

    return {
        "message": "Logout successful"
    }


# =========================
# REFRESH ACCESS TOKEN
# =========================

def refresh_access_token(
    refresh_token: str,
    db: Session
):
    # Verify refresh token
    user_id = verify_refresh_token(
        refresh_token
    )

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired refresh token"
        )

    # Convert user ID
    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    # Find user
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    # Check stored refresh token
    if user.refresh_token != refresh_token:
        raise HTTPException(
            status_code=401,
            detail="Refresh token has been revoked"
        )

    # Create new access token
    new_access_token = create_access_token(
        user.id
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }


# =========================
# UPDATE PROFILE
# =========================

def update_profile(
    profile: UserProfileUpdate,
    current_user: User,
    db: Session
):
    # Check username
    existing_username = db.query(User).filter(
        User.username == profile.username,
        User.id != current_user.id
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Check email
    existing_email = db.query(User).filter(
        User.email == profile.email,
        User.id != current_user.id
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Update user
    current_user.username = profile.username
    current_user.email = profile.email

    db.commit()
    db.refresh(current_user)

    return current_user


# =========================
# CHANGE PASSWORD
# =========================

def change_password(
    passwords: ChangePassword,
    current_user: User,
    db: Session
):
    # Check old password
    password_correct = verify_password(
        passwords.current_password,
        current_user.password_hash
    )

    if not password_correct:
        raise HTTPException(
            status_code=400,
            detail="Current password is incorrect"
        )

    # Hash new password
    current_user.password_hash = hash_password(
        passwords.new_password
    )

    # Invalidate refresh token
    current_user.refresh_token = None

    db.commit()

    return {
        "message": "Password changed successfully"
    }