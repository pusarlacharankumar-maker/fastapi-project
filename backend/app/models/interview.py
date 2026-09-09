from sqlalchemy import Column, Integer, String, Text

from app.config.database import Base


class Interview(Base):

    __tablename__ = "interviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question = Column(
        Text,
        nullable=False
    )

    answer = Column(
        Text,
        nullable=False
    )

    explanation = Column(
        Text,
        nullable=True
    )

    category = Column(
        String(100),
        nullable=False
    )

    difficulty = Column(
        String(50),
        nullable=False
    )