from datetime import datetime
from pydantic import BaseModel

class CampaignBase(BaseModel):
    name: str
    description: str

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    display_name: str = "Tav"

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    campaigns: list[Campaign] = []

    class Config:
        orm_mode = True