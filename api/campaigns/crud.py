from sqlalchemy.orm import Session

from ..models import Campaign
from ..schemas import CampaignCreate

def get_all_campaigns(db: Session, skip: int = 0):
    return db.query(Campaign).offset(skip).all()

def get_user_campaigns(db: Session, user_id: int):
    return db.query(Campaign).filter_by(user_id=user_id).all()

def create_user_campaign(db: Session, campaign: CampaignCreate, user_id: int):
    campaign = Campaign(**campaign.model_dump(), user_id=user_id)
    db.add(campaign)
    db.commit()
    db.refresh(campaign)

    return campaign