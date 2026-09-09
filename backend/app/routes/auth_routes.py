from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.dependencies import get_current_user
from app.models import User

from app.schemas import (
    UserRegister,
    UserLogin,
    UserResponse,
    TokenResponse,
    RefreshTokenRequest,
    AccessTokenResponse,
    UserProfileUpdate,
    ChangePassword
)

from app.services.auth_service import (
    register_user,
    login_user,
    logout_user,
    refresh_access_token,
    update_profile,
    change_password
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
    return register_user(
        user,
        db
    )


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
    return login_user(
        user,
        db
    )


# =========================
# CURRENT USER
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
    return logout_user(
        current_user,
        db
    )


# =========================
# REFRESH ACCESS TOKEN
# =========================

@router.post(
    "/refresh",
    response_model=AccessTokenResponse
)
def refresh(
    token_data: RefreshTokenRequest,
    db: Session = Depends(get_db)
):
    return refresh_access_token(
        token_data.refresh_token,
        db
    )


# =========================
# UPDATE PROFILE
# =========================

@router.put(
    "/profile",
    response_model=UserResponse
)
def profile(
    profile_data: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_profile(
        profile_data,
        current_user,
        db
    )


# =========================
# CHANGE PASSWORD
# =========================

@router.put(
    "/change-password"
)
def password(
    passwords: ChangePassword,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return change_password(
        passwords,
        current_user,
        db
    )