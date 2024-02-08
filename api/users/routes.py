from typing import Any, Annotated

from fastapi import APIRouter, Depends, HTTPException

from auth.oauth import oauth2_scheme
from .auth import get_current_user
from users.schemas import UserCreate, UserSchema

user = APIRouter(
    prefix="/users",
    
)

@user.get("/health", tags=["Users"])
def check_health() -> str:
    return "ok"

# TODO: figure out if you want to protect this with client/secret or not. Would rather not have open api 
## NOTE: this is a decision/iteration out of scope of MVP
@user.post("/",  response_model=UserSchema, response_description="The created user.",  tags=["Users"])
def create_user(user: UserCreate): # TODO: def don't return the password
    """
    Create a User with all the information:
    - **username**: each user must have an email to log in with; their email is their username.
    - **display_name**: An optional name for the user to display in the UI.
    """
    # TODO: if user exists already, throw a 403
    return user

# NOTE: tutorial, remember that order MATTERS
@user.get("/me", response_model=UserSchema, tags=["Users"])
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_user)]
):
    return current_user

@user.get("/{user_id}", tags=["Users"])
def get_user(user_id: int, token: Annotated[str, Depends(oauth2_scheme)]):
    if not user_id: # expand to check db if there is none, this should never trigger rn
        raise HTTPException(status_code=404, detail="Item not found")
    return {"user_id": user_id}
