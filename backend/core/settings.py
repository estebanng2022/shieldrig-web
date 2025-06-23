import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key: str = "SUPER_SECRET_KEY"
    algorithm: str = "HS256"

settings = Settings()
