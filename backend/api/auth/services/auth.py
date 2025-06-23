from sqlmodel import select
from backend.database.session import get_session
from backend.models.user import User
from backend.utils.security import verify_password
from backend.utils.jwt import create_access_token

def authenticate(username: str, password: str):
    with get_session() as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user or not verify_password(password, user.hashed_password):
            return None
        token = create_access_token({'sub': user.username, 'role': user.role})
        return token, user.permissions
