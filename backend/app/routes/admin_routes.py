from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.dependencies import get_current_user
from app.models import User

from app.middleware.admin_middleware import get_current_admin

from app.schemas import UserResponse

from app.services.admin_service import (
    get_all_users,
    delete_user
)


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


# =========================
# GET ALL USERS
# ADMIN ONLY
# =========================

@router.get(
    "/users",
    response_model=list[UserResponse]
)
def users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return get_all_users(db)


# =========================
# DELETE USER
# ADMIN ONLY
# =========================

@router.delete(
    "/users/{user_id}"
)
def remove_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return delete_user(
        user_id,
        db
    )