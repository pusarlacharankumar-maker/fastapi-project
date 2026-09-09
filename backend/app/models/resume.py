from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=True
    )

    education = Column(
        Text,
        nullable=True
    )

    skills = Column(
        Text,
        nullable=True
    )

    experience = Column(
        Text,
        nullable=True
    )

    projects = Column(
        Text,
        nullable=True
    )

    certifications = Column(
        Text,
        nullable=True
    )

    location = Column(
        String(150),
        nullable=True
    )

    career_objective = Column(
        Text,
        nullable=True
    )

    achievements = Column(
        Text,
        nullable=True
    )

    linkedin_url = Column(
        String(500),
        nullable=True
    )

    github_url = Column(
        String(500),
        nullable=True
    )

    user = relationship("User")