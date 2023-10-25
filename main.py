import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from database import db
from config import config



logger = logging.getLogger(__name__)

API_PREFIX = "/api/v1"

@asynccontextmanager
async def lifespan(app: FastAPI):

    db.connect(config.DB_CONFIG)
    yield

    await db.disconnect()


def init_app():
    app = FastAPI(
        title="DMs Codex",
        description="Handling Our Stuff",
        version="1",
        lifespan=lifespan
    )

    # TODO: see if theres a cleaner file structure that I can pull all of these from one place
    # maybe like api/__init__.py or routers.py and all the users, sessions, etc folders under the api dir
    from api.users.views import user_api

    app.include_router(
        user_api,
        prefix=API_PREFIX,
    )

    return app


app = init_app()