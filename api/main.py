from fastapi import FastAPI
from users.routes import user

API_PREFIX = "/api/v1"

app = FastAPI()

app.include_router(user, prefix=API_PREFIX)

@app.get("/")
async def root() -> str:
    return "ok"