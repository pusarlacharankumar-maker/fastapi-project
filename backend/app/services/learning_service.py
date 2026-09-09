from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Course, Lesson
from app.schemas import (
    CourseCreate,
    CourseUpdate,
    LessonCreate,
    LessonUpdate
)


# =========================
# COURSE
# =========================

def create_course(
    course_data: CourseCreate,
    db: Session
):
    course = Course(
        title=course_data.title,
        description=course_data.description
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


def get_courses(db: Session):
    return db.query(Course).all()


def get_course(
    course_id: int,
    db: Session
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


def update_course(
    course_id: int,
    course_data: CourseUpdate,
    db: Session
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    course.title = course_data.title
    course.description = course_data.description

    db.commit()
    db.refresh(course)

    return course


def delete_course(
    course_id: int,
    db: Session
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(course)
    db.commit()

    return {
        "message": "Course deleted successfully"
    }


# =========================
# LESSON
# =========================

def create_lesson(
    lesson_data: LessonCreate,
    db: Session
):
    course = db.query(Course).filter(
        Course.id == lesson_data.course_id
    ).first()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    lesson = Lesson(
        course_id=lesson_data.course_id,
        title=lesson_data.title,
        notes=lesson_data.notes,
        important_concepts=lesson_data.important_concepts,
        youtube_url=lesson_data.youtube_url
    )

    db.add(lesson)
    db.commit()
    db.refresh(lesson)

    return lesson


def get_lessons(
    course_id: int,
    db: Session
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return db.query(Lesson).filter(
        Lesson.course_id == course_id
    ).all()


def get_lesson(
    lesson_id: int,
    db: Session
):
    lesson = db.query(Lesson).filter(
        Lesson.id == lesson_id
    ).first()

    if lesson is None:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found"
        )

    return lesson


def update_lesson(
    lesson_id: int,
    lesson_data: LessonUpdate,
    db: Session
):
    lesson = db.query(Lesson).filter(
        Lesson.id == lesson_id
    ).first()

    if lesson is None:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found"
        )

    lesson.title = lesson_data.title
    lesson.notes = lesson_data.notes
    lesson.important_concepts = lesson_data.important_concepts
    lesson.youtube_url = lesson_data.youtube_url

    db.commit()
    db.refresh(lesson)

    return lesson


def delete_lesson(
    lesson_id: int,
    db: Session
):
    lesson = db.query(Lesson).filter(
        Lesson.id == lesson_id
    ).first()

    if lesson is None:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found"
        )

    db.delete(lesson)
    db.commit()

    return {
        "message": "Lesson deleted successfully"
    }