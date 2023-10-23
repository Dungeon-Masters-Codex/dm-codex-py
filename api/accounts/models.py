from datetime import datetime

from api import bcrypt, db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    display_name = db.Column(db.String, nullable=False, default="Tav")
    created_date = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    # TODO: set init constructor class, feels a little off to do so