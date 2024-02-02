from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth = APIRouter(prefix="/auth")

# NOTE: going to build this in /user/routes and it may stay living there
@auth.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # get username from form_data => form_data.username
    # if not user dict, raise 400
    # get hashed password
    # if not password raise 400
    # return access token (username) and token type (string bearer) 
    pass