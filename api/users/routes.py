from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

user = APIRouter(
    prefix="/users"
)

class User(BaseModel):
    # TODO: when more relevant expand to using Field for email/password
    email: str # TODO: install python-email-validator to get the EmailStr type and later validation

# TODO: review fastapi docs that this is a sensible pattern when more time
class UserInput(User):
    """ Extends User with input specific schema. """
    password: str
    display_name: str | None = Field(
        default=None, title="The display name chosen by the user", 
        max_length=50,
        examples=["Elrich of the Emerald Enclave"]
    )

@user.get("/health")
def check_health() -> str:
    return "ok"

@user.post("/", response_model=User)
def create_user(user: UserInput) -> Any: # TODO: def don't return the password
    return user

@user.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}