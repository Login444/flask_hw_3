from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), nullable=False)
    user_lastname = db.Column(db.String(80), nullable=False)
    user_email = db.Column(db.String(80), unique=True, nullable=False)
    user_password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'User({self.user_name}, {self.user_lastname}, {self.user_email})'
