from src import db
from src.models.users import User


def is_email_registered(email):
    return db.session.query(User.id).filter_by(email=email).first() is not None


def register_user(first, last, email, password):
    user = User(first=first, last=last, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    

def are_credentials_valid(email, password):
    return db.session.query(User.id).filter_by(email=email, password=password).first() is not None