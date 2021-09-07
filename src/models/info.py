from src import db


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    cover = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(100), nullable=False)
    resume_path = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    direction = db.Column(db.String(50), nullable=False)
    linkedin_url = db.Column(db.String(200), nullable=False)
    github_url = db.Column(db.String(200), nullable=False)
    instagram_url = db.Column(db.String(200), nullable=False)
    facebook_url = db.Column(db.String(200), nullable=False)
