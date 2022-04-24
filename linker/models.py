from datetime import datetime
from . import db, bcrypt


# users model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    joined_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User({self.fullname}, {self.username}, {self.email})"

    @staticmethod
    def encrypt_password(password):
        return bcrypt.generate_password_hash(password)
