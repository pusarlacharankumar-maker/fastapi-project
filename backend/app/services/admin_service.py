from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User


def get_all_users(db: Session):
    return db.query(User).all()


def delete_user(user_id: int, db: Session):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }