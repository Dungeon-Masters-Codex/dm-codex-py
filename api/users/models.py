

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field

from db.database import Base

class User(BaseModel):
    # TODO: when more relevant expand to using Field for email/password
    username: str # TODO: install python-email-validator to get the EmailStr type and later validation (will be presented as email to user in FE)
    display_name: str | None = Field(
        default=None, title="The display name chosen by the user", 
        max_length=50,
        examples=["Elrich of the Emerald Enclave"]
    )

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
     # TODO: install python-email-validator to get the EmailStr type and later validation (will be presented as email to user in FE)
    username = Column(String, unique=True, nullable=False) 
    hashed_password = Column(String, nullable=False)
    display_name = Column(String(25), nullable=False, default="Tav")
    created_date = Column(DateTime)

    # NOTE: keeping this here in the event I need it later but that is in doubt
    # def __init__(self, email, password, display_name, is_admin=False):
    #     self.email = email
    #     self.password = bcrypt.generate_password_hash(password)
    #     self.display_name = display_name
    #     self.created_on = datetime.now()
    #     self.is_admin = is_admin

    def __repr__(self):
        return f"<User '{self.display_name}': {self.email}"

