from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models import User
from app.schemas import (
    UserRegister,
    UserResponse,
    UserLogin,
    TokenResponse,
    UserProfileUpdate,
    ChangePassword
)
from app.dependencies import get_current_user
from app.services.auth_service import (
    register_user,
    login_user
)
from app.utils.password import (
    hash_password,
    verify_password
)
from app.utils.jwt import (
    verify_token,
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =========================
# REGISTER
# =========================

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(user, db)


# =========================
# LOGIN
# =========================

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(user, db)


# =========================
# GET CURRENT USER
# =========================

@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user


# =========================
# LOGOUT
# =========================

@router.post("/logout")
def logout(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # Remove refresh token
    current_user.refresh_token = None

    db.commit()

    return {
        "message": "Logout successful"
    }


# =========================
# UPDATE PROFILE
# =========================

@router.put(
    "/profile",
    response_model=UserResponse
)
def update_profile(
    profile: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
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

    # Update
    current_user.username = profile.username
    current_user.email = profile.email

    db.commit()
    db.refresh(current_user)

    return current_user


# =========================
# CHANGE PASSWORD
# =========================

@router.put("/change-password")
def change_password(
    passwords: ChangePassword,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # Check current password
    if not verify_password(
        passwords.current_password,
        current_user.password_hash
    ):
        raise HTTPException(
            status_code=400,
            detail="Current password is incorrect"
        )

    # Hash new password
    current_user.password_hash = hash_password(
        passwords.new_password
    )

    # Optional security:
    # invalidate old refresh token
    current_user.refresh_token = None

    db.commit()

    return {
        "message": "Password changed successfully"
    }


# =========================
# REFRESH ACCESS TOKEN
# =========================

@router.post("/refresh")
def refresh_access_token(
    refresh_token: str = Body(..., embed=True),
    db: Session = Depends(get_db)
):

    # Verify refresh token
    user_id = verify_token(refresh_token)

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired refresh token"
        )

    # Find user
    user = db.query(User).filter(
        User.id == int(user_id)
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
            detail="Invalid refresh token"
        )

    # Create new access token
    new_access_token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }