from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models import User
from app.schemas import (
    CourseCreate,
    CourseUpdate,
    LessonCreate,
    LessonUpdate,
    CourseResponse,
    LessonResponse
)

from app.middleware.admin_middleware import get_current_admin

from app.services.learning_service import (
    create_course,
    get_courses,
    get_course,
    update_course,
    delete_course,
    create_lesson,
    get_lessons,
    get_lesson,
    update_lesson,
    delete_lesson
)


router = APIRouter(
    prefix="/learning",
    tags=["Learning"]
)


# =========================
# COURSES
# =========================

@router.post(
    "/courses",
    response_model=CourseResponse
)
def add_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return create_course(course, db)


@router.get(
    "/courses",
    response_model=list[CourseResponse]
)
def courses(
    db: Session = Depends(get_db)
):
    return get_courses(db)


@router.get(
    "/courses/{course_id}",
    response_model=CourseResponse
)
def course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return get_course(course_id, db)


@router.put(
    "/courses/{course_id}",
    response_model=CourseResponse
)
def edit_course(
    course_id: int,
    course_data: CourseUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return update_course(
        course_id,
        course_data,
        db
    )


@router.delete(
    "/courses/{course_id}"
)
def remove_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return delete_course(
        course_id,
        db
    )


# =========================
# LESSONS
# =========================

@router.post(
    "/lessons",
    response_model=LessonResponse
)
def add_lesson(
    lesson: LessonCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return create_lesson(
        lesson,
        db
    )


@router.get(
    "/courses/{course_id}/lessons",
    response_model=list[LessonResponse]
)
def lessons(
    course_id: int,
    db: Session = Depends(get_db)
):
    return get_lessons(
        course_id,
        db
    )


@router.get(
    "/lessons/{lesson_id}",
    response_model=LessonResponse
)
def lesson(
    lesson_id: int,
    db: Session = Depends(get_db)
):
    return get_lesson(
        lesson_id,
        db
    )


@router.put(
    "/lessons/{lesson_id}",
    response_model=LessonResponse
)
def edit_lesson(
    lesson_id: int,
    lesson_data: LessonUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return update_lesson(
        lesson_id,
        lesson_data,
        db
    )


@router.delete(
    "/lessons/{lesson_id}"
)
def remove_lesson(
    lesson_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return delete_lesson(
        lesson_id,
        db
    )