from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

from accounts.routes import accounts_bp
from accounts.models import User

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

@app.route('/')
def base():
    return "Dungeon Master\'s Codex API"

# Registering blueprints
app.register_blueprint(accounts_bp)