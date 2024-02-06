from fastapi import FastAPI

from models import Base
from database import SessionLocal, engine
from auth.routes import auth
from users.routes import user
from constants.api import API_PREFIX

app = FastAPI()

app.include_router(auth, prefix=API_PREFIX)
app.include_router(user, prefix=API_PREFIX)

@app.get("/")
async def root() -> str:
    return "Dungeon Master\'s Codex API"
