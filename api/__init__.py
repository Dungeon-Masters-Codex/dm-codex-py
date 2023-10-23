from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate # may just use alembic
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
# migrate = Migrate(app, db) # see comment above

# Registering blueprints
from accounts.routes import accounts_bp

app.register_blueprint(accounts_bp)