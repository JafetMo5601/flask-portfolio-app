from dataclasses import dataclass

from src import db


@dataclass
class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    # Add year
