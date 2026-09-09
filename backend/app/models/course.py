from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.config.database import Base


class Course(Base):

    __tablename__ = "courses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(150),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    category = Column(
        String(100),
        nullable=True
    )

    level = Column(
        String(50),
        nullable=True
    )

    lessons = relationship(
        "Lesson",
        back_populates="course",
        cascade="all, delete-orphan"
    )