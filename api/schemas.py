from datetime import datetime
from pydantic import BaseModel

class CampaignBase(BaseModel):
    name: str
    description: str

class CampaignCreate(CampaignBase):
    created_date: datetime = datetime.now()

class CampaignSchema(CampaignBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True

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