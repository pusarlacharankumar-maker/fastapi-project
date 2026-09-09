from sqlalchemy import Column, Integer, String, Text

from app.config.database import Base


class Placement(Base):
    __tablename__ = "placements"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company_name = Column(
        String(150),
        nullable=False
    )

    job_title = Column(
        String(150),
        nullable=False
    )

    location = Column(
        String(150),
        nullable=True
    )

    job_type = Column(
        String(50),
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    skills_required = Column(
        Text,
        nullable=True
    )

    salary = Column(
        String(100),
        nullable=True
    )

    application_url = Column(
        String(500),
        nullable=True
    )