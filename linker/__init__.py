import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config import DevConfig, ProdConfig


app = Flask(__name__)
if os.getenv("FLASK_ENV") == "development":
    app.config.from_object(DevConfig)
elif os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProdConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Please login to access the requested page"
login_manager.login_message_category = "info"

from . import routes
