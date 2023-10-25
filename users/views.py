from flask import Blueprint
from flask_login import current_user, login_user

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return "Update me this isn't what I would return to the FE"

@accounts_bp.route("/login")
def login():
    pass

@accounts_bp.route("/logout")
def logout():
    pass