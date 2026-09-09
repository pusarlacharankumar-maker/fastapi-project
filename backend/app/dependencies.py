from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import ast

from app.config.database import get_db
from app.models import User
from app.utils.jwt import verify_token


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    # Verify JWT
    user_id = verify_token(token)

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    # Handle case where verify_token returns:
    # "{'sub': '2'}"
    if isinstance(user_id, str):

        user_id = user_id.strip()

        if user_id.startswith("{") and user_id.endswith("}"):

            try:
                payload = ast.literal_eval(user_id)
                user_id = payload.get("sub")

            except (ValueError, SyntaxError):
                raise HTTPException(
                    status_code=401,
                    detail="Invalid token payload"
                )

    # Convert user ID to integer
    try:
        user_id = int(user_id)

    except (ValueError, TypeError):
        raise HTTPException(
            status_code=401,
            detail="Invalid user ID in token"
        )

    # Find user
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user