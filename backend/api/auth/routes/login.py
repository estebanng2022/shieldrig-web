from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from backend.api.auth.services.auth import authenticate

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    permissions: list[str]

@router.post('/login', response_model=LoginResponse)
def login(data: LoginRequest):
    result = authenticate(data.username, data.password)
    if not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales invalidas")
    token, perms = result
    return {"access_token": token, "permissions": perms}
