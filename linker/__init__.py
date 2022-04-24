import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config import DevConfig, ProdConfig


app = Flask(__name__)
if os.getenv("FLASK_ENV") == "development":
    app.config.from_object(DevConfig)
elif os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProdConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from . import routes
