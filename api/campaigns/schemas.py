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