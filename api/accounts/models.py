from datetime import datetime

from bcrypt import hashpw
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from database import Base

class Questions(Base):

    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index =True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    display_name = Column(String, nullable=False, default="Tav")
    created_date = Column(DateTime, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    def __init__(self, email, password, display_name, is_admin=False):
        self.email = email
        self.password = hashpw(password)
        self.display_name = display_name
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<User '{self.display_name}': {self.email}"