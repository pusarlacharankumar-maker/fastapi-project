from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.config.database import Base, engine

from app.models import (
    User,
    Course,
    Lesson,
    Progress,
    Interview,
    Resume,
    Placement
)

from app.routes.auth_routes import router as auth_router
from app.routes.learning_routes import router as learning_router
from app.routes.interview_routes import router as interview_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.resume_routes import router as resume_router
from app.routes.placement_routes import router as placement_router
from app.routes.admin_routes import router as admin_router
from app.routes.progress_routes import router as progress_router

from app.middleware.error_middleware import (
    http_exception_handler,
    general_exception_handler
)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CodeSphere API",
    description="Backend API for the CodeSphere student platform",
    version="1.0.0"
)


# Error handlers
app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler
)

app.add_exception_handler(
    Exception,
    general_exception_handler
)


# Routes
app.include_router(auth_router)
app.include_router(learning_router)
app.include_router(interview_router)
app.include_router(dashboard_router)
app.include_router(resume_router)
app.include_router(placement_router)
app.include_router(admin_router)
app.include_router(progress_router)


@app.get("/")
def root():
    return {
        "message": "CodeSphere Backend is running"
    }