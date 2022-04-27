from flask import render_template, url_for, redirect, abort, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from linker import app, db
from linker.models import User, Link
from linker.form import SignUpForm, LoginForm, LinksForm

# ROUTES
@app.route("/")
@app.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("links"))
    return render_template("home.html", title="HOME")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="CONTACT")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("links"))
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
    if current_user.is_authenticated:
        return redirect(url_for("links"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and User.check_password(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Welcome {user.fullname}, You have logged in", "info")
            next = request.args.get("next")
            return redirect(next) if next else redirect(url_for("links"))
        else:
            flash("Incorrect username or password", "warn")
    return render_template("login.html", title="LOGIN", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out successfully", "info")
    return redirect(url_for("home"))


@app.route("/links", methods=["GET", "POST"])
@login_required
def links():
    form = LinksForm()
    linksInDb = Link.query.get(current_user.id)
    if request.method == "POST":
        data = request.get_json()
        try:
            if not linksInDb:
                linksObj = Link(
                    portfolio=data.get("portfolio"),
                    github=data.get("github"),
                    linkedin=data.get("linkedin"),
                    codepen=data.get("codepen"),
                    twitter=data.get("twitter"),
                    user_id=current_user.id,
                )
                db.session.add(linksObj)
                db.session.commit()
            else:
                linksInDb.portfolio = data.get("portfolio")
                linksInDb.github = data.get("github")
                linksInDb.linkedin = data.get("linkedin")
                linksInDb.codepen = data.get("codepen")
                linksInDb.twitter = data.get("twitter")
                db.session.commit()
            return {"status": 200, "msg": "Links have been updated"}
        except:
            return {"status": 404, "msg": "Sorry, links were not saved"}
    elif request.method == "GET":
        form.portfolio.data = linksInDb.portfolio
        form.github.data = linksInDb.github
        form.linkedin.data = linksInDb.linkedin
        form.codepen.data = linksInDb.codepen
        form.twitter.data = linksInDb.twitter
    return render_template("links.html", title="LINKS", form=form)


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html", title="ACCOUNT")
