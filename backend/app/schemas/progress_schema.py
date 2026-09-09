from pydantic import BaseModel, Field


class ProgressCreate(BaseModel):
    lesson_id: int
    completion_percentage: float = Field(ge=0, le=100)


class ProgressResponse(BaseModel):
    id: int
    lesson_id: int
    completion_percentage: float

    class Config:
        from_attributes = True