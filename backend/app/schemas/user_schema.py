from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=72
    )


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=72
    )


class UserProfileUpdate(BaseModel):
    username: str
    email: EmailStr


class ChangePassword(BaseModel):
    current_password: str
    new_password: str = Field(
        min_length=8,
        max_length=72
    )


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str