import bcrypt
from datetime import datetime
from sqlalchemy.orm import Session

from ..models import User
from ..schemas import UserCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter_by(user_id=user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter_by(email=email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    # TODO: implement env var for gensalt
    hashed_password = bcrypt.hashpw(user.password, bcrypt.gensalt(12))
    new_user = User(
        email=user.email, 
        password=hashed_password, 
        display_name=user.display_name,
        created_date=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


