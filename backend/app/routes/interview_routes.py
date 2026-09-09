from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models import User

from app.schemas import (
    InterviewCreate,
    InterviewUpdate,
    InterviewResponse
)

from app.middleware.admin_middleware import (
    get_current_admin
)

from app.services.interview_service import (
    create_interview,
    get_interviews,
    get_interviews_by_category,
    get_interviews_by_difficulty,
    get_interview,
    update_interview,
    delete_interview
)


router = APIRouter(
    prefix="/interviews",
    tags=["Interview Preparation"]
)


# =========================
# CREATE QUESTION
# ADMIN ONLY
# =========================

@router.post(
    "",
    response_model=InterviewResponse
)
def add_interview(
    interview: InterviewCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return create_interview(
        interview,
        db
    )


# =========================
# GET ALL QUESTIONS
# PUBLIC
# =========================

@router.get(
    "",
    response_model=list[InterviewResponse]
)
def interviews(
    db: Session = Depends(get_db)
):
    return get_interviews(db)


# =========================
# GET BY CATEGORY
# PUBLIC
# =========================

@router.get(
    "/category/{category}",
    response_model=list[InterviewResponse]
)
def interviews_by_category(
    category: str,
    db: Session = Depends(get_db)
):
    return get_interviews_by_category(
        category,
        db
    )


# =========================
# GET BY DIFFICULTY
# PUBLIC
# =========================

@router.get(
    "/difficulty/{difficulty}",
    response_model=list[InterviewResponse]
)
def interviews_by_difficulty(
    difficulty: str,
    db: Session = Depends(get_db)
):
    return get_interviews_by_difficulty(
        difficulty,
        db
    )


# =========================
# GET ONE QUESTION
# PUBLIC
# =========================

@router.get(
    "/{interview_id}",
    response_model=InterviewResponse
)
def interview(
    interview_id: int,
    db: Session = Depends(get_db)
):
    return get_interview(
        interview_id,
        db
    )


# =========================
# UPDATE QUESTION
# ADMIN ONLY
# =========================

@router.put(
    "/{interview_id}",
    response_model=InterviewResponse
)
def edit_interview(
    interview_id: int,
    interview_data: InterviewUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return update_interview(
        interview_id,
        interview_data,
        db
    )


# =========================
# DELETE QUESTION
# ADMIN ONLY
# =========================

@router.delete(
    "/{interview_id}"
)
def remove_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return delete_interview(
        interview_id,
        db
    )