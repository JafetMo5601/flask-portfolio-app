from flask import send_from_directory, current_app
import os

from src.models.projects import Project
from src.models.awards import Award
from src.models.info import Info
from src import db


def get_info():
    if Info.query.filter(Info.id == 1).first() is not None:
        response = [dict(list((info.__dict__).items())[1:])
                    for info in Info.query.all()]
        remove_files(response[0])
        return response[0], 200
    else:
        return 'Not found.', 404


def get_projects():
    try:
        response = [dict(list((project.__dict__).items())[1:])
                    for project in Project.query.all()]
        return response, 200
    except:
        return 'There was an internal server error.', 500


def get_awards():
    try:
        response = [dict(list((award.__dict__).items())[1:])
                    for award in Award.query.all()]
        return response, 200
    except:
        return 'There was an internal server error.', 500


def get_resume():
    try:
        return send_from_directory(current_app.config['UPLOAD_FOLDER'] + 'resume\\', 'resume.pdf'), 200
    except:
        return 'Not found.', 404


def get_image(image_name, image_type):
    try:
        image_path = os.path.join(
            current_app.config['UPLOAD_FOLDER'], ('images\\' + image_type))
        image_name = [name for name in os.listdir(
            image_path) if image_name.replace(' ', '_') in name][0]
        return send_from_directory(image_path, image_name), 200
    except:
        return 'Bad request.', 400


def remove_files(response):
    del response['resume_path']
    del response['cover']
    del response['photo']
