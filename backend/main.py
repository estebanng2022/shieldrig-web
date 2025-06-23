from fastapi import FastAPI
from database import create_db_and_tables

app = FastAPI()

create_db_and_tables()

@app.get("/")
def root():
    return {"message": "ShieldRig Backend is running with SQLite!"}
