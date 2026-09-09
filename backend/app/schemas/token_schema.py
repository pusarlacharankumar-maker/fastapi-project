from pydantic import BaseModel


# =========================
# LOGIN TOKEN RESPONSE
# =========================

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


# =========================
# REFRESH TOKEN REQUEST
# =========================

class RefreshTokenRequest(BaseModel):
    refresh_token: str


# =========================
# NEW ACCESS TOKEN RESPONSE
# =========================

class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"