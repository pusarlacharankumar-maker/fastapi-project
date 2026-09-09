from pydantic import BaseModel, Field


# =========================
# CREATE RESUME
# =========================

class ResumeCreate(BaseModel):

    full_name: str = Field(
        min_length=2,
        max_length=100
    )

    phone: str | None = Field(
        default=None,
        max_length=20
    )

    education: str | None = None

    skills: str | None = None

    experience: str | None = None

    projects: str | None = None

    certifications: str | None = None

    location: str | None = Field(
        default=None,
        max_length=150
    )

    career_objective: str | None = None

    achievements: str | None = None

    linkedin_url: str | None = Field(
        default=None,
        max_length=500
    )

    github_url: str | None = Field(
        default=None,
        max_length=500
    )


# =========================
# UPDATE RESUME
# =========================

class ResumeUpdate(BaseModel):

    full_name: str = Field(
        min_length=2,
        max_length=100
    )

    phone: str | None = Field(
        default=None,
        max_length=20
    )

    education: str | None = None

    skills: str | None = None

    experience: str | None = None

    projects: str | None = None

    certifications: str | None = None

    location: str | None = Field(
        default=None,
        max_length=150
    )

    career_objective: str | None = None

    achievements: str | None = None

    linkedin_url: str | None = Field(
        default=None,
        max_length=500
    )

    github_url: str | None = Field(
        default=None,
        max_length=500
    )


# =========================
# RESUME RESPONSE
# =========================

class ResumeResponse(BaseModel):

    id: int

    user_id: int

    full_name: str

    phone: str | None

    education: str | None

    skills: str | None

    experience: str | None

    projects: str | None

    certifications: str | None

    location: str | None

    career_objective: str | None

    achievements: str | None

    linkedin_url: str | None

    github_url: str | None

    class Config:
        from_attributes = True