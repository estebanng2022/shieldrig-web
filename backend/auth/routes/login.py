# backend/auth/routes/login.py
from fastapi import APIRouter, HTTPException
from models.user import User

router = APIRouter()

# Usuario temporal (tú)
fake_owner = User(username="esteban", password="password123", role="owner")

@router.post("/login")
def login(user: User):
    if user.username == fake_owner.username and user.password == fake_owner.password:
        return {"message": "✅ Autenticado como owner"}
    else:
        raise HTTPException(status_code=401, detail="⚠️ Credenciales incorrectas")
