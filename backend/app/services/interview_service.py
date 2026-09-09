from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Interview

from app.schemas.interview_schema import (
    InterviewCreate,
    InterviewUpdate
)


# =========================
# CREATE QUESTION
# =========================

def create_interview(
    interview_data: InterviewCreate,
    db: Session
):
    interview = Interview(
        question=interview_data.question,
        answer=interview_data.answer,
        category=interview_data.category,
        difficulty=interview_data.difficulty
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview


# =========================
# GET ALL QUESTIONS
# =========================

def get_interviews(
    db: Session
):
    return db.query(Interview).all()


# =========================
# GET BY CATEGORY
# =========================

def get_interviews_by_category(
    category: str,
    db: Session
):
    return db.query(Interview).filter(
        Interview.category.ilike(category)
    ).all()


# =========================
# GET BY DIFFICULTY
# =========================

def get_interviews_by_difficulty(
    difficulty: str,
    db: Session
):
    return db.query(Interview).filter(
        Interview.difficulty.ilike(difficulty)
    ).all()


# =========================
# GET ONE QUESTION
# =========================

def get_interview(
    interview_id: int,
    db: Session
):
    interview = db.query(Interview).filter(
        Interview.id == interview_id
    ).first()

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview question not found"
        )

    return interview


# =========================
# UPDATE QUESTION
# =========================

def update_interview(
    interview_id: int,
    interview_data: InterviewUpdate,
    db: Session
):
    interview = db.query(Interview).filter(
        Interview.id == interview_id
    ).first()

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview question not found"
        )

    interview.question = interview_data.question
    interview.answer = interview_data.answer
    interview.category = interview_data.category
    interview.difficulty = interview_data.difficulty

    db.commit()
    db.refresh(interview)

    return interview


# =========================
# DELETE QUESTION
# =========================

def delete_interview(
    interview_id: int,
    db: Session
):
    interview = db.query(Interview).filter(
        Interview.id == interview_id
    ).first()

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview question not found"
        )

    db.delete(interview)
    db.commit()

    return {
        "message": "Interview question deleted successfully"
    }