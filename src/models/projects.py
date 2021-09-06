from src import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(50), nullable=False)
    tools = db.Column(db.String(300), nullable=False)