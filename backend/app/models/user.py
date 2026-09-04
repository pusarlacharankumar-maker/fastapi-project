from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.config.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = Column(
        String,
        nullable=False
    )

    refresh_token = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )