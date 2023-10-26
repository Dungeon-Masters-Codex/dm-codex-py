from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    display_name = Column(String, nullable=False, default="Tav")
    created_date = Column(DateTime, nullable=False)

    # NOTE: keeping this here in the event I need it later but that is in doubt
    # def __init__(self, email, password, display_name, is_admin=False):
    #     self.email = email
    #     self.password = bcrypt.generate_password_hash(password)
    #     self.display_name = display_name
    #     self.created_on = datetime.now()
    #     self.is_admin = is_admin

    def __repr__(self):
        return f"<User '{self.display_name}': {self.email}"

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text(250))
    created_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="campaigns")