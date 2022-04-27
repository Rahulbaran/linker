from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import EmailField, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, InputRequired, ValidationError, Regexp
from .models import User

# SIGNUP FORM
class SignUpForm(FlaskForm):
    fullname = StringField(
        "Fullname",
        validators=[InputRequired(), Length(min=5, max=255, message="name should be 5 to 255 characters long")],
    )
    username = StringField(
        "Username",
        validators=[
            InputRequired(),
            Length(min=5, max=100, message="username should be 5 to 100 characters long"),
        ],
    )
    email = EmailField(
        "Email",
        validators=[InputRequired(), Length(min=10, max=255, message="email should be 10 to 255 characters long")],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8, max=50, message="password should be 8 to 50 characters long")],
    )
    recaptcha = RecaptchaField()
    submit = SubmitField("Signup")

    # Validation Methods
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("username is already taken")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("email is already registered")

    def validate_password(self, password):
        specialChar = "!@#$%^&*()_+-=|\}]{[:;?/>.<,~`\"'"
        totalSpecial = 0
        for char in password.data:
            if char in specialChar:
                totalSpecial += 1
        if not totalSpecial:
            raise ValidationError("password should contain atleast one special character")


# LOGIN FORM
class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=5, max=100, message="username should be 5 to 100 characters long")],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8, max=50, message="password should be 8 to 50 characters long")],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


# LINKS FORM
class LinksForm(FlaskForm):
    portfolio = StringField(
        "Portfolio",
        validators=[
            Length(min=10, max=50, message="portfolio link should be 10 to 50 characters long"),
        ],
    )
    github = StringField(
        "Github",
        validators=[
            InputRequired(),
            Length(min=20, max=50, message="github profile link should be 20 to 50 characters long"),
        ],
    )
    linkedin = StringField(
        "Linkedin",
        validators=[Length(min=20, max=100, message="linkedin profile link should be 20 to 100 characters long")],
    )
    codepen = StringField(
        "Codepen",
        validators=[Length(min=20, max=50, message="codepen profile link should be 20 to 50 characters long")],
    )
    twitter = StringField(
        "Twitter",
        validators=[Length(min=20, max=50, message="twitter profile link should be 20 to 50 characters long")],
    )
    submit = SubmitField("Add Links")
