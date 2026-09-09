from pydantic import BaseModel, EmailStr, Field


# =========================
# REGISTER
# =========================

class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


# =========================
# LOGIN
# =========================

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=72)


# =========================
# USER RESPONSE
# =========================

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_admin: bool

    class Config:
        from_attributes = True


# =========================
# UPDATE PROFILE
# =========================

class UserProfileUpdate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr


# =========================
# CHANGE PASSWORD
# =========================

class ChangePassword(BaseModel):
    current_password: str = Field(min_length=1, max_length=72)
    new_password: str = Field(min_length=8, max_length=72)