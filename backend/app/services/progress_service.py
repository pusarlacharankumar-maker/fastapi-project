from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Progress, Lesson


# =========================
# UPDATE LESSON PROGRESS
# =========================

def update_progress(
    user_id: int,
    lesson_id: int,
    completion_percentage: float,
    db: Session
):
    # Check lesson
    lesson = db.query(Lesson).filter(
        Lesson.id == lesson_id
    ).first()

    if lesson is None:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found"
        )

    # Check existing progress
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.lesson_id == lesson_id
    ).first()

    if progress:
        progress.completion_percentage = completion_percentage

    else:
        progress = Progress(
            user_id=user_id,
            lesson_id=lesson_id,
            completion_percentage=completion_percentage
        )

        db.add(progress)

    db.commit()
    db.refresh(progress)

    return progress


# =========================
# GET ALL USER PROGRESS
# =========================

def get_user_progress(
    user_id: int,
    db: Session
):
    return db.query(Progress).filter(
        Progress.user_id == user_id
    ).all()


# =========================
# GET LESSON PROGRESS
# =========================

def get_lesson_progress(
    user_id: int,
    lesson_id: int,
    db: Session
):
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.lesson_id == lesson_id
    ).first()

    if progress is None:
        raise HTTPException(
            status_code=404,
            detail="Progress not found"
        )

    return progress