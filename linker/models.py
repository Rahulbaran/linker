from datetime import datetime
from . import db, bcrypt, login_manager


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
    joined_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

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
