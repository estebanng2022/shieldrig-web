
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

# CORS para permitir llamadas del frontend (ajustar en prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto a tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para login request
class LoginRequest(BaseModel):
    email: str
    password: str

# Modelo para login response
class LoginResponse(BaseModel):
    token: str
    user: dict

# Endpoint de login
@app.post("/auth/login", response_model=LoginResponse)
def login_user(data: LoginRequest):
    # Aquí pondrías validación real contra DB
    if data.email == "admin@shieldrig.com" and data.password == "password123":
        return LoginResponse(
            token="dummy-jwt-token-123456",
            user={"id": 1, "email": data.email, "role": "owner"}
        )
    raise HTTPException(status_code=401, detail="Invalid credentials")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
