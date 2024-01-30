from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from models import Base
from database import SessionLocal, engine
from users.routes import user

API_PREFIX = "/api/v1"

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(user, prefix=API_PREFIX)

@app.get("/")
async def root() -> str:
    return "Dungeon Master\'s Codex API"