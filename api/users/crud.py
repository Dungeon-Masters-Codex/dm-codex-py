import bcrypt
from datetime import datetime
from sqlalchemy.orm import Session

from .models import User
from .schemas import UserCreate
from campaigns.schemas import CampaignSchema, CampaignCreate

# NOTE: Steps to create utility functions to create data
## Create a SQL Alchemy model instance with your data
## `add` that instance object to your db session
## `commit` the changes to the db (so they are saved)
## `refresh` your instance (so that it contains any new data from db, like generated id)

def get_user(db: Session, user_id: int):
    return db.query(User).filter_by(user_id=user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter_by(username=username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    # TODO: implement env var for gensalt
    # TODO: make sure not returning users password, even hashed
    hashed_password = bcrypt.hashpw(user.password, bcrypt.gensalt(12))
    new_user = User(
        username=user.username, 
        password=hashed_password, 
        display_name=user.display_name,
        created_date=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def create_user_campaign(db: Session, campaign: CampaignCreate, user_id: int):
    db_campaign = CampaignSchema(**campaign.model_dump(), user_id=user_id)
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    
    return db_campaign

