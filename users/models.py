from datetime import datetime
from uuid import uuid4

from bcrypt import hashpw
from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.sql import expression as sql

from database import Base



class User(Base):

    __tablename__ = "users"

    id = Column(String, primary_key=True, index =True)
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

    @classmethod
    async def create(cls, db, **kwargs) -> "User":
        query = (
            sql.insert(cls)
            .values(id=str(uuid4()), **kwargs)
            .returning(cls.id, cls.full_name)
        )
        users = await db.execute(query)
        await db.commit()
        return users.first()

    @classmethod
    async def update(cls, db, id, **kwargs) -> "User":
        query = (
            sql.update(cls)
            .where(cls.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
            .returning(cls.id, cls.full_name)
        )
        users = await db.execute(query)
        await db.commit()
        return users.first()

    @classmethod
    async def get(cls, db, id) -> "User":
        query = sql.select(cls).where(cls.id == id)
        users = await db.execute(query)
        (user,) = users.first()
        return user

    @classmethod
    async def get_all(cls, db) -> list["User"]:
        query = sql.select(cls)
        users = await db.execute(query)
        users = users.scalars().all()
        return users

    @classmethod
    async def delete(cls, db, id) -> bool:
        query = (
            sql.delete(cls)
            .where(cls.id == id)
            .returning(
                cls.id,
                cls.full_name,
            )
        )
        await db.execute(query)
        await db.commit()
        return True