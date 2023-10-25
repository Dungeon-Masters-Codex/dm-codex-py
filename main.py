import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from database import db
from config import config



logger = logging.getLogger(__name__)

API_PREFIX = "/api/v1"

def init_app():
    app = FastAPI(
        title="DMs Codex",
        description="Handling Our Stuff",
        version="1"
    )

    from api.users.views import user_api

    app.include_router(
        user_api,
        prefix=API_PREFIX,
    )

    @app.get("/health")
    async def health() -> str:
        return "ok"

    return app


app = init_app()