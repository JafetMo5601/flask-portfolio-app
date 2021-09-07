from src.models.projects import Project
from src.models.awards import Award
from src.models.info import Info
from src import db


def get_info():
    if Info.query.filter(Info.id == 1).first() is not None:
        response = [dict(list((info.__dict__).items())[1:]) for info in Info.query.all()]
        return response, 200
    else: 
        return 'Info not found.', 404


def get_projects():
    try: 
        response = [dict(list((project.__dict__).items())[1:]) for project in Project.query.all()]
        return response, 200
    except: 
        return 'There was an internal server error.', 500
    

def get_awards():
    try: 
        response = [dict(list((award.__dict__).items())[1:]) for award in Award.query.all()]
        return response, 200
    except: 
        return 'There was an internal server error.', 500   