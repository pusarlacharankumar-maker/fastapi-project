from pydantic import BaseModel, Field


# =========================
# CREATE INTERVIEW QUESTION
# =========================

class InterviewCreate(BaseModel):
    question: str = Field(
        min_length=5
    )

    answer: str = Field(
        min_length=1
    )

    category: str = Field(
        min_length=2,
        max_length=100
    )

    difficulty: str = Field(
        min_length=2,
        max_length=50
    )


# =========================
# UPDATE INTERVIEW QUESTION
# =========================

class InterviewUpdate(BaseModel):
    question: str = Field(
        min_length=5
    )

    answer: str = Field(
        min_length=1
    )

    category: str = Field(
        min_length=2,
        max_length=100
    )

    difficulty: str = Field(
        min_length=2,
        max_length=50
    )


# =========================
# INTERVIEW RESPONSE
# =========================

class InterviewResponse(BaseModel):
    id: int
    question: str
    answer: str
    category: str
    difficulty: str

    class Config:
        from_attributes = True