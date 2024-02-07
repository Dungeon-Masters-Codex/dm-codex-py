from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import SessionLocal
from auth.routes import auth
from users.routes import user
from constants.api import API_PREFIX

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(auth, prefix=API_PREFIX)
app.include_router(user, prefix=API_PREFIX)

## CORS ##
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    # NOTE: will need to add production when we get there
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root() -> str:
    return "Dungeon Master\'s Codex API"
