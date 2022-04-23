from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import EmailField, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, InputRequired, ValidationError, Regexp

# SIGNUP FORM
class SignUpForm(FlaskForm):
    fullname = StringField(
        "Fullname",
        validators=[
            InputRequired(),
            Length(min=5, max=255, message="name should be 5 to 255 characters long"),
            Regexp(r"^[A-Za-z\s]{5, 255}$", message="name should only contain alphabats"),
        ],
    )
    username = StringField(
        "Username",
        validators=[
            InputRequired(),
            Length(min=5, max=100, message="username should be 5 to 100 characters long"),
            Regexp(r"^\w{5, 100}$", message="username should only contain alphabats, numbers & underscores"),
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


# LOGIN FORM
class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            InputRequired(),
            Length(min=5, max=100, message="username should be 5 to 100 characters long"),
            Regexp(r"^\w{5, 100}$", message="username should only contain alphabats, numbers & underscores"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8, max=50, message="password should be 8 to 50 characters long")],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
