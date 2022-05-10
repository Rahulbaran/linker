from datetime import datetime
from linker import db, bcrypt, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# users model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    avatar = db.Column(db.String(50), nullable=False, default="default.png")
    about_me = db.Column(db.Text, nullable=False, default="A Frontend Web Developer")
    joined_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    urls = db.relationship("Link", backref="user_links", cascade="all, delete", lazy="dynamic")

    # Methods for working with flask-login package
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"User({self.fullname}, {self.username}, {self.email})"

    @staticmethod
    def encrypt_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(user_password, entered_password):
        return bcrypt.check_password_hash(user_password, entered_password)


# links model
class Link(db.Model):
    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    portfolio = db.Column(db.String(50))
    github = db.Column(db.String(50), nullable=False)
    linkedin = db.Column(db.String(100))
    codepen = db.Column(db.String(50))
    twitter = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"({self.portfolio}, {self.github}, {self.linkedin}, {self.codepen}, {self.twitter})"
