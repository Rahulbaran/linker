from flask import render_template, url_for, redirect, abort, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from . import app, db
from .models import User
from .form import SignUpForm, LoginForm

# ROUTES
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="HOME")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="CONTACT")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            fullname=form.fullname.data,
            username=form.username.data,
            email=form.email.data,
            password=User.encrypt_password(form.password.data),
        )
        db.session.add(user)
        db.session.commit()
        flash("You have been registerd successfully", "info")
        return redirect(url_for("login"))
    return render_template("signup.html", title="SIGNUP", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="LOGIN", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
