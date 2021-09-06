from flask import jsonify
import json

from src.models.projects import Project
from src.models.awards import Award
from src.models.info import Info
from src import db


def add_info(
    about, description, resume, phone, email, direction, linkedin, gh, insta, fb):
    try: 
        info = Info(
            about=about, description=description, resume_path=resume, phone=phone, email=email, direction=direction, linkedin_url=linkedin, github_url=gh, instagram_url=insta, facebook_url=fb)
        db.session.add(info)
        db.session.commit()
        return 'Info added succesfully.', 200
    except: 
        return 'There was an internal server error.', 500


def get_info():
    if Info.query.filter(Info.id == 1).first() is not None:
        response = [dict(list((info.__dict__).items())[1:]) for info in Info.query.all()]
        return response, 200
    else: 
        return 'Info not found.', 404


def remove_info(id):
    if Info.query.filter(Info.id == id).first() is not None:
        Info.query.filter(Info.id == id).delete()
        db.session.commit()
        return 'Info removed successfully', 200
    else: 
        return 'Info not found', 404


def update_info(
    id, about, description, resume, phone, email, direction, linkedin, gh, insta, fb):
    if Info.query.filter(Info.id == id).first() is not None:
        Info.query.filter(Info.id == id).update(
            {
                Info.about: about,
                Info.description: description,
                Info.resume_path: resume,
                Info.phone: phone,
                Info.email: email,
                Info.direction: direction,
                Info.linkedin_url: linkedin,
                Info.github_url: gh,
                Info.instagram_url: insta,
                Info.facebook_url: fb     
            }
        )
        db.session.commit()
        return 'Info updated successfully', 200
    else: 
        return 'Info not found', 404


def add_project(title, description, tools, image):
    try:
        project = Project(title=title, description=description, image_path=image, tools=tools)
        db.session.add(project)
        db.session.commit()
        return 'Project added succesfully.', 200
    except: 
        return 'There was an internal server error.', 500


def get_projects():
    try: 
        response = [dict(list((project.__dict__).items())[1:]) for project in Project.query.all()]
        return response, 200
    except: 
        return 'There was an internal server error.', 500


def remove_project(id):
    if Project.query.filter(Project.id == id).first() is not None:
        Project.query.filter(Project.id == id).delete()
        db.session.commit()
        return 'Project removed successfully', 200
    else: 
        return 'Project not found', 404


def update_project(id, title, description, tools, image):
    if Project.query.filter(Project.id == id).first() is not None:
        Project.query.filter(Project.id == id).update(
            {
                Project.title: title, 
                Project.description: description,
                Project.tools : tools, 
                Project.image_path : image
            }
        )
        db.session.commit()
        return 'Project updated successfully', 200
    else: 
        return 'Project not found', 404


def add_award(title, description):
    try:
        award = Award(title=title, description=description)
        db.session.add(award)
        db.session.commit()
        return 'Award added succesfully.', 200
    except: 
        return 'There was an internal server error.', 500


def get_awards():
    try: 
        response = [dict(list((award.__dict__).items())[1:]) for award in Award.query.all()]
        return response, 200
    except: 
        return 'There was an internal server error.', 500


def remove_award(id):
    if Award.query.filter(Award.id == id).first() is not None:
        Award.query.filter(Award.id == id).delete()
        db.session.commit()
        return 'Award removed successfully', 200
    else: 
        return 'Award not found', 404


def update_award(id, title, description):
    if Award.query.filter(Award.id == id).first() is not None:
        Award.query.filter(Award.id == id).update(
            {
                Award.title: title,
                Award.description: description
            }
        )
        db.session.commit()
        return 'Award updated successfully', 200
    else: 
        return 'Award not found', 404
    
