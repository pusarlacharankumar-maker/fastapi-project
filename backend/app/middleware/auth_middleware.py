from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        # Authentication is handled by
        # app.dependencies.get_current_user

        response = await call_next(request)

        return response