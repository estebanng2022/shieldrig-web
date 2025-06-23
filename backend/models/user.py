from sqlmodel import SQLModel, Field
from typing import Optional
import json
from config.roles import OWNER_ROLE, DEFAULT_OWNER_PERMISSIONS

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    role: str = OWNER_ROLE
    permissions: str = Field(default_factory=lambda: json.dumps(DEFAULT_OWNER_PERMISSIONS))
