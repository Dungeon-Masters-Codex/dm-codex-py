from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel

user = APIRouter(
    prefix="/users"
)

@user.get("/health")
def check_health() -> str:
    return "ok"