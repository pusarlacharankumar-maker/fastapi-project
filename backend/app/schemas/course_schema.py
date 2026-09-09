from pydantic import BaseModel, Field


class CourseCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None


class CourseUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str | None

    class Config:
        from_attributes = True