from datetime import datetime

from flask_login import UserMixin

from api import bcrypt, db

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    display_name = db.Column(db.String, nullable=False, default="Tav")
    created_date = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, display_name, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.display_name = display_name
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f"<User '{self.display_name}': {self.email}"