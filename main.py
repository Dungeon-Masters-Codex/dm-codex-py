from database import db
from fastapi import FastAPI
from config import config
import uvicorn
import logging


logger = logging.getLogger(__name__)

API_PREFIX = "/api/v1"


def init_app():
    app = FastAPI(
        title="Users App",
        description="Handling Our User",
        version="1",
    )

    # TODO: this is deprecated, update me
    @app.on_event("startup")
    def startup():
        db.connect(config.DB_CONFIG)

    @app.on_event("shutdown")
    async def shutdown():
        await db.disconnect()

    # TODO: see if theres a cleaner file structure that I can pull all of these from one place
    # maybe like api/__init__.py or routers.py and all the users, sessions, etc folders under the api dir
    from users.views import user_api

    app.include_router(
        user_api,
        prefix=API_PREFIX,
    )

    return app


app = init_app()