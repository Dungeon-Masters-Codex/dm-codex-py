from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from users.auth import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from .schemas import Token

from constants.api import API_PREFIX, AUTH_PREFIX

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{API_PREFIX}{AUTH_PREFIX}/token")

auth = APIRouter(
    prefix=AUTH_PREFIX
)

@auth.post("/token", tags=["Auth"])
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")