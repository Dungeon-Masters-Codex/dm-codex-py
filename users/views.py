from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from users.models import User
from database import db


class UserSchema(BaseModel):
    email: str
    password: str
    display_name: str



class UserSerializer(BaseModel):
    id: str
    email: str
    password: str
    display_name: str


    class Config:
        from_attributes = True


user_api = APIRouter(
    prefix="/users",
)


@user_api.post("/")
async def create_user(
    user: UserSchema, db_session=Depends(db.get_db)
) -> UserSerializer:
    user = await User.create(db_session, **user.dict())
    return user


@user_api.get("/{id}")
async def get_user(id: str, db_session=Depends(db.get_db)) -> UserSerializer:
    user = await User.get(db_session, id)
    return user


@user_api.get("/")
async def get_all_users(db_session=Depends(db.get_db)) -> List[UserSerializer]:
    users = await User.get_all(db_session)
    return users


@user_api.put("/{id}")
async def update(
    id: str, user: UserSchema, db_session=Depends(db.get_db)
) -> UserSerializer:
    user = await User.update(db_session, id, **user.dict())
    return user


@user_api.delete("/{id}")
async def delete_user(id: str, db_session=Depends(db.get_db)) -> bool:
    return await User.delete(db_session, id)