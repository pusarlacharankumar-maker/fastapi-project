from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User, Progress, Resume


def get_all_users(db: Session):
    return db.query(User).all()


def delete_user(user_id: int, db: Session, current_user_id: int | None = None):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if current_user_id is not None and user.id == current_user_id:
        raise HTTPException(
            status_code=400,
            detail="You cannot delete your own account"
        )

    if user.is_admin:
        admin_count = db.query(User).filter(
            User.is_admin.is_(True)
        ).count()

        if admin_count <= 1:
            raise HTTPException(
                status_code=400,
                detail="At least one admin account must remain"
            )

    db.query(Progress).filter(
        Progress.user_id == user_id
    ).delete(synchronize_session=False)

    db.query(Resume).filter(
        Resume.user_id == user_id
    ).delete(synchronize_session=False)

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }