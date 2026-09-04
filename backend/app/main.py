from fastapi import FastAPI

from app.routes.auth_routes import router as auth_router


# Create FastAPI application
app = FastAPI(
    title="CodeSphere API",
    description="Backend API for CodeSphere",
    version="1.0.0"
)


# =========================
# ROUTES
# =========================

app.include_router(auth_router)


# =========================
# HOME
# =========================

@app.get("/")
def home():
    return {
        "message": "CodeSphere API is running"
    }