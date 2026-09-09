from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.dependencies import get_current_user
from app.models import User

from app.schemas.resume_schema import (
    ResumeCreate,
    ResumeUpdate,
    ResumeResponse
)

from app.services.resume_service import (
    create_or_update_resume,
    get_my_resume,
    update_resume,
    delete_resume
)


router = APIRouter(
    prefix="/resumes",
    tags=["Resume"]
)


# =========================
# CREATE OR UPDATE RESUME
# =========================

@router.post(
    "",
    response_model=ResumeResponse
)
def save_resume(
    resume_data: ResumeCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_or_update_resume(
        current_user.id,
        resume_data,
        db
    )


# =========================
# GET MY RESUME
# =========================

@router.get(
    "/me",
    response_model=ResumeResponse
)
def my_resume(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_my_resume(
        current_user.id,
        db
    )


# =========================
# UPDATE MY RESUME
# =========================

@router.put(
    "/me",
    response_model=ResumeResponse
)
def edit_resume(
    resume_data: ResumeUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_resume(
        current_user.id,
        resume_data,
        db
    )


# =========================
# DELETE MY RESUME
# =========================

@router.delete("/me")
def remove_resume(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return delete_resume(
        current_user.id,
        db
    )