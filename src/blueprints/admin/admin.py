from werkzeug.utils import secure_filename
from flask import current_app
import requests
import os

from src.models.projects import Project
from src.models.awards import Award
from src.models.info import Info
from src import db


def add_info(
        about, description, cover, photo, resume, phone, email, direction, linkedin, gh, insta, fb):
    try:
        if not there_is_info():
            if cover == '' or photo == '' or resume == '':
                return 'Bad request.', 400
            
            cover_path = save_image(cover, 'info', 'cover')
            photo_path = save_image(photo, 'info', 'photo')
            resume_path = save_resume(resume)
            
            info = Info(
                about=about, description=description, cover=cover_path, photo=photo_path, resume_path=resume_path, phone=phone, email=email, direction=direction, linkedin_url=linkedin, github_url=gh, instagram_url=insta, facebook_url=fb)
            db.session.add(info)
            db.session.commit()
            return 'Ok.', 200
        else:
            return 'Conflict.', 409
    except:
        return 'There was an internal server error.', 500


def update_info(
        about, description, cover, photo, resume, phone, email, direction, linkedin, gh, insta, fb):
    if Info.query.filter(Info.id == 1).first() is not None:
        
        cover = retrieve_image('cover', 'info') if (cover == '') else save_image(cover, 'info', 'cover')
        photo = retrieve_image('photo', 'info') if (photo == '') else save_image(photo, 'info', 'photo')
        resume = retrieve_resume() if (resume == '') else save_resume(resume)
        
        Info.query.filter(Info.id == 1).update(
            {
                Info.about: about,
                Info.description: description,
                Info.cover: cover,
                Info.photo: photo,
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
        return 'Ok', 200
    else:
        return 'Not found', 404


def remove_info():
    if Info.query.filter(Info.id == 1).first() is not None:
        Info.query.filter(Info.id == 1).delete()
        db.session.commit()
        remove_image('cover', 'info')
        remove_image('photo', 'info')
        remove_resume()
        return 'Ok', 200
    else:
        return 'Not found', 404


def add_project(title, description, tools, image):
    try:
        if image == None:
            return 'Bad request.' , 400
        image_path = save_image(image, 'projects', title)
        project = Project(title=title, description=description,
                          image_path=image_path, tools=tools)
        db.session.add(project)
        db.session.commit()
        return 'Ok.', 200
    except:
        return 'There was an internal server error.', 500


def update_project(id, title, description, tools, image):
    if Project.query.filter(Project.id == id).first() is not None:
        
        image_path = retrieve_image(title, 'projects') if (image == '') else save_image(image, 'projects', title)
        
        Project.query.filter(Project.id == id).update(
            {
                Project.title: title,
                Project.description: description,
                Project.tools: tools,
                Project.image_path: image_path
            }
        )
        db.session.commit()
        return 'Ok.', 200
    else:
        return 'Not found', 404


def remove_project(id):
    project = Project.query.filter(Project.id == id).first()
    if project is not None:
        Project.query.filter(Project.id == id).delete()
        db.session.commit()
        remove_image(project.title.replace(' ', '_'), 'projects')
        return 'Ok.', 200
    else:
        return 'Not found', 404


def add_award(title, description, year):
    try:
        award = Award(title=title, description=description, year=year)
        db.session.add(award)
        db.session.commit()
        return 'Ok.', 200
    except:
        return 'There was an internal server error.', 500


def remove_award(id):
    if Award.query.filter(Award.id == id).first() is not None:
        Award.query.filter(Award.id == id).delete()
        db.session.commit()
        return 'Ok.', 200
    else:
        return 'Not found', 404


def update_award(id, title, description):
    if Award.query.filter(Award.id == id).first() is not None:
        Award.query.filter(Award.id == id).update(
            {
                Award.title: title,
                Award.description: description
            }
        )
        db.session.commit()
        return 'Ok.', 200
    else:
        return 'Not found.', 404


def save_image(image, image_type, image_name):    
    if image and image.filename != '':
        image_name = change_file_name(secure_filename(image.filename), image_name.replace(' ', '_'))
        image_path = current_app.config['UPLOAD_FOLDER'] + 'images\\' + image_type
        image_path = os.path.join(image_path, image_name)
        image.save(image_path)
        return image_path
    else:
        return ''
    

def save_resume(resume):
    resume_path = current_app.config['UPLOAD_FOLDER'] + 'resume'

    if resume and resume.filename != '':
        resume_name = change_file_name(secure_filename(resume.filename), 'resume')
        resume_path = os.path.join(resume_path, resume_name)
        resume.save(resume_path)
        return resume_path
    else:
        return ''


def add_award_cover(image):
    try:
        awards_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 'images\\awards')
        if len(os.listdir(awards_path)) > 1:
            file = [file for file in os.listdir(awards_path) if 'awards' in file]
            os.remove(file)
        save_image(image, 'awards', 'awards')
        return 'Ok.', 200
    except:
        return 'There was an internal server error', 500


def change_file_name(old_name, new_name):
    ext = os.path.splitext(old_name)[1]
    return new_name + ext


def retrieve_resume():
    resume_path = current_app.config['UPLOAD_FOLDER'] + 'resume\\'
    resume_name = [name for name in os.listdir(resume_path) if 'resume' in name]
    resume_path += resume_name[0] 
    return resume_path


def retrieve_image(image_name, image_type):
    image_path = current_app.config['UPLOAD_FOLDER'] + 'images\\' + image_type + '\\'
    image_name = [name for name in os.listdir(image_path) if image_name.replace(' ', '_') in name]
    image_path += image_name[0] 
    return image_path


def remove_image(image_name, image_type):
    image_path = current_app.config['UPLOAD_FOLDER'] + 'images\\' + image_type + '\\'
    image_name = [name for name in os.listdir(image_path) if image_name.replace(' ', '_') in name]
    os.remove(image_path + image_name[0])


def remove_resume():
    resume_path = current_app.config['UPLOAD_FOLDER'] + 'resume\\'
    resume_name = [name for name in os.listdir(resume_path) if 'resume' in name]
    os.remove(resume_path + resume_name[0])
    
    
def there_is_info():
    return len(Info.query.all()) > 0