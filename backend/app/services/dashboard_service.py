from sqlalchemy.orm import Session

from app.models import (
    User,
    Course,
    Lesson,
    Progress,
    Resume,
    Placement,
    Interview
)


def get_dashboard(
    user_id: int,
    db: Session
):

    # Get current user
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        return {
            "message": "User not found"
        }

    # Courses
    total_courses = db.query(Course).count()

    # Lessons
    total_lessons = db.query(Lesson).count()

    # User progress
    progress_records = db.query(Progress).filter(
        Progress.user_id == user_id
    ).all()

    lessons_started = len(progress_records)

    lessons_completed = sum(
        1
        for progress in progress_records
        if progress.completion_percentage >= 100
    )

    if progress_records:
        average_progress = (
            sum(
                progress.completion_percentage
                for progress in progress_records
            )
            / len(progress_records)
        )
    else:
        average_progress = 0

    # Resume
    resume = db.query(Resume).filter(
        Resume.user_id == user_id
    ).first()

    # Placements
    total_placements = db.query(
        Placement
    ).count()

    # Interview questions
    total_interview_questions = db.query(
        Interview
    ).count()

    return {
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_admin": user.is_admin
        },

        "courses": {
            "total_courses": total_courses,
            "total_lessons": total_lessons
        },

        "learning_progress": {
            "lessons_started": lessons_started,
            "lessons_completed": lessons_completed,
            "average_progress": round(
                average_progress,
                2
            )
        },

        "resume": {
            "created": resume is not None,
            "resume_id": (
                resume.id
                if resume
                else None
            )
        },

        "placements": {
            "total": total_placements
        },

        "interview_preparation": {
            "total_questions": total_interview_questions
        }
    }