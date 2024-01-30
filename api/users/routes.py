from typing import Any, Annotated

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from auth.oauth import oauth2_scheme

user = APIRouter(
    prefix="/users"
)

class User(BaseModel):
    # TODO: when more relevant expand to using Field for email/password
    email: str # TODO: install python-email-validator to get the EmailStr type and later validation
    display_name: str | None = Field(
        default=None, title="The display name chosen by the user", 
        max_length=50,
        examples=["Elrich of the Emerald Enclave"]
    )

# TODO: review fastapi docs that this is a sensible pattern when more time
class UserInput(User):
    """ Extends User with input specific schema. """
    password: str


@user.get("/health")
def check_health() -> str:
    return "ok"

@user.post("/",  response_model=User, response_description="The created user.",  tags=["Users"])
def create_user(user: UserInput, token: Annotated[str, Depends(oauth2_scheme)],) -> Any: # TODO: def don't return the password
    """
    Create a User with all the information:
    - **email**: each user must have an email to log in with.
    - **display_name**: An optional name for the user to display in the UI.
    """
    # TODO: if user exists already, throw a 403
    return user

@user.get("/{user_id}")
def get_user(user_id: int, token: Annotated[str, Depends(oauth2_scheme)], tags=["Users"]):
    if not user_id: # expand to check db if there is none, this should never trigger rn
        raise HTTPException(status_code=404, detail="Item not found")
    return {"user_id": user_id}