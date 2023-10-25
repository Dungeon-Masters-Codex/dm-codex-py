from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel

class UserSchema(BaseModel):
    email: str
    password: str
    display_name: str


user = APIRouter(
    prefix="/users"
)

@user.get("/health")
def check_health() -> str:
    return "ok"