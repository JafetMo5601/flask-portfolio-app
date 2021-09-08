from flask import send_from_directory, current_app
import os

from src.models.projects import Project
from src.models.awards import Award
from src.models.info import Info
from src import db


def get_info():
    if Info.query.filter(Info.id == 1).first() is not None:
        response = [dict(list((info.__dict__).items())[1:]) for info in Info.query.all()]
        remove_files(response[0])
        return response[0], 200
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
    
    
def get_resume():
    return send_from_directory(current_app.config['UPLOAD_FOLDER'] + 'resume\\', 'resume.pdf')


def get_cover():
    cover_path = current_app.config['UPLOAD_FOLDER'] + 'images\\info\\'
    cover_name = os.listdir(cover_path)[0]
    print(cover_name)
    return send_from_directory(cover_path, cover_name)


def get_photo():
    photo_path = current_app.config['UPLOAD_FOLDER'] + 'images\\info\\'
    photo_name = os.listdir(photo_path)[1]
    print(photo_name)
    return send_from_directory(photo_path, photo_name)


def remove_files(response):
    del response['resume_path']
    del response['cover']
    del response['photo']
    