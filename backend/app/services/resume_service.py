from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Resume
from app.schemas.resume_schema import ResumeCreate, ResumeUpdate


# =========================
# CREATE OR UPDATE RESUME
# =========================

def create_or_update_resume(
    user_id: int,
    resume_data: ResumeCreate,
    db: Session
):
    resume = db.query(Resume).filter(
        Resume.user_id == user_id
    ).first()

    if resume is None:
        resume = Resume(
            user_id=user_id
        )

        db.add(resume)

    resume.full_name = resume_data.full_name
    resume.phone = resume_data.phone
    resume.education = resume_data.education
    resume.skills = resume_data.skills
    resume.experience = resume_data.experience
    resume.projects = resume_data.projects
    resume.certifications = resume_data.certifications
    resume.location = resume_data.location
    resume.career_objective = resume_data.career_objective
    resume.achievements = resume_data.achievements
    resume.linkedin_url = resume_data.linkedin_url
    resume.github_url = resume_data.github_url

    db.commit()
    db.refresh(resume)

    return resume


# =========================
# GET MY RESUME
# =========================

def get_my_resume(
    user_id: int,
    db: Session
):
    resume = db.query(Resume).filter(
        Resume.user_id == user_id
    ).first()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return resume


# =========================
# UPDATE MY RESUME
# =========================

def update_resume(
    user_id: int,
    resume_data: ResumeUpdate,
    db: Session
):
    resume = db.query(Resume).filter(
        Resume.user_id == user_id
    ).first()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    resume.full_name = resume_data.full_name
    resume.phone = resume_data.phone
    resume.education = resume_data.education
    resume.skills = resume_data.skills
    resume.experience = resume_data.experience
    resume.projects = resume_data.projects
    resume.certifications = resume_data.certifications
    resume.location = resume_data.location
    resume.career_objective = resume_data.career_objective
    resume.achievements = resume_data.achievements
    resume.linkedin_url = resume_data.linkedin_url
    resume.github_url = resume_data.github_url

    db.commit()
    db.refresh(resume)

    return resume


# =========================
# DELETE MY RESUME
# =========================

def delete_resume(
    user_id: int,
    db: Session
):
    resume = db.query(Resume).filter(
        Resume.user_id == user_id
    ).first()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    db.delete(resume)
    db.commit()

    return {
        "message": "Resume deleted successfully"
    }