from src import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(30), nullable=False)
    last = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
