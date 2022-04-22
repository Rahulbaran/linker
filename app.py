import os
from flask import Flask, render_template, url_for, redirect, abort, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import DevConfig, ProdConfig

app = Flask(__name__)
if os.getenv("FLASK_ENV") == "development":
    app.config.from_object(DevConfig)
elif os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProdConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)

# ROUTES
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="HOME")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html", title="SIGNUP")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", title="LOGIN")


# RUNNING APP IN PYTHONIC WAY
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True, load_dotenv=True)
