from pydantic import BaseModel, Field


# =========================
# CREATE PLACEMENT
# =========================

class PlacementCreate(BaseModel):

    company_name: str = Field(
        min_length=2,
        max_length=150
    )

    job_title: str = Field(
        min_length=2,
        max_length=150
    )

    location: str | None = Field(
        default=None,
        max_length=150
    )

    job_type: str | None = Field(
        default=None,
        max_length=50
    )

    description: str | None = None

    skills_required: str | None = None

    salary: str | None = Field(
        default=None,
        max_length=100
    )

    application_url: str | None = Field(
        default=None,
        max_length=500
    )


# =========================
# UPDATE PLACEMENT
# =========================

class PlacementUpdate(BaseModel):

    company_name: str = Field(
        min_length=2,
        max_length=150
    )

    job_title: str = Field(
        min_length=2,
        max_length=150
    )

    location: str | None = Field(
        default=None,
        max_length=150
    )

    job_type: str | None = Field(
        default=None,
        max_length=50
    )

    description: str | None = None

    skills_required: str | None = None

    salary: str | None = Field(
        default=None,
        max_length=100
    )

    application_url: str | None = Field(
        default=None,
        max_length=500
    )


# =========================
# PLACEMENT RESPONSE
# =========================

class PlacementResponse(BaseModel):

    id: int
    company_name: str
    job_title: str
    location: str | None
    job_type: str | None
    description: str | None
    skills_required: str | None
    salary: str | None
    application_url: str | None

    class Config:
        from_attributes = True