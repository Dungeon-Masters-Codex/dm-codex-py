from datetime import datetime

from pydantic import BaseModel

from campaigns.schemas import CampaignSchema

class UserBase(BaseModel):
    email: str
    display_name: str = "Tav"

class UserCreate(UserBase):
    password: str

class UserSchema(UserBase):
    id: int
    created_date: datetime = datetime.now()
    campaigns: list[CampaignSchema] = []

    class Config:
        orm_mode = True

class UserInDB(UserBase):
    hashed_password: str