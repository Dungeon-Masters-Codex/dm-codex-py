# TODO: after I get familiar with the flow here, break these out of main
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# TODO: found a little nudge on medium to cover gaps I had in the db stack:
# https://python.plainenglish.io/fastapi-sqlalchemy-2-0-pydantic-v2-alembic-postgres-and-docker-2c429acfc333