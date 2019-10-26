from application import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):

    __tablename__ = 'fuksit'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), index=False, unique=False, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    admin = db.Column(db.Boolean, index=False, unique=False, nullable=False)

    def set_password(self, password):
        """Hash password"""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'

