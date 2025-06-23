from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.user import User
from database import get_session
from auth.auth_handler import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/signup")
def signup(username: str, password: str, session: Session = Depends(get_session)):
    user_exists = session.exec(select(User).where(User.username == username)).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")
    user = User(username=username, hashed_password=hash_password(password))
    session.add(user)
    session.commit()
    return {"message": "User created successfully"}

@router.post("/login")
def login(username: str, password: str, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
