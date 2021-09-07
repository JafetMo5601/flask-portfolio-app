from werkzeug.utils import secure_filename
import os

from src.models.projects import Project
from src.models.awards import Award
from src.models.info import Info
from src import db


def add_info(
        about, description, cover, photo, resume, phone, email, direction, linkedin, gh, insta, fb):
    try:
        if cover == '' or photo == '' or resume == '':
            return 'Bad request.', 400
        info = Info(
            about=about, description=description, cover=cover, photo=photo, resume_path=resume, phone=phone, email=email, direction=direction, linkedin_url=linkedin, github_url=gh, instagram_url=insta, facebook_url=fb)
        db.session.add(info)
        db.session.commit()
        return 'Info added succesfully.', 200
    except:
        return 'There was an internal server error.', 500


def remove_info(id):
    if Info.query.filter(Info.id == id).first() is not None:
        Info.query.filter(Info.id == id).delete()
        db.session.commit()
        remove_cover()
        remove_photo()
        remove_resume()
        return 'Info removed successfully', 200
    else:
        return 'Info not found', 404


def update_info(
        id, about, description, cover, photo, resume, phone, email, direction, linkedin, gh, insta, fb):
    if Info.query.filter(Info.id == id).first() is not None:
        Info.query.filter(Info.id == id).update(
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
        return 'Info updated successfully', 200
    else:
        return 'Info not found', 404


def add_project(title, description, tools, image):
    try:
        project = Project(title=title, description=description,
                          image_path=image, tools=tools)
        db.session.add(project)
        db.session.commit()
        return 'Project added succesfully.', 200
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
                Project.tools: tools,
                Project.image_path: image
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


def save_image(image, is_photo=False):
    image_path = os.getcwd() + '\\src\\files_storage\\images\\info'

    if image and image.filename != '':
        if is_photo:
            image_name = change_photo_name(secure_filename(image.filename))
        else:
            image_name = change_cover_name(secure_filename(image.filename))

        image_path = os.path.join(image_path, image_name)
        image.save(image_path)
        return image_path
    else:
        return ''
    

def save_resume(resume):
    resume_path = os.getcwd() + '\\src\\files_storage\\resume'

    if resume and resume.filename != '':
        resume_name = change_resume_name(secure_filename(resume.filename))
        resume_path = os.path.join(resume_path, resume_name)
        resume.save(resume_path)
        print(resume_path)
        return resume_path
    else:
        return ''


def change_photo_name(old_name):
    ext = os.path.splitext(old_name)[1]
    return 'photo' + ext


def change_cover_name(old_name):
    ext = os.path.splitext(old_name)[1]
    return 'cover' + ext


def change_resume_name(old_name):
    ext = os.path.splitext(old_name)[1]
    return 'resume' + ext


def retrieve_cover():
    cover_path = os.getcwd() + '\\src\\files_storage\\images\\info\\'
    cover_name = [name for name in os.listdir(cover_path) if 'cover' in name]
    cover_path += cover_name[0] 
    return cover_path


def retrieve_photo():
    photo_path = os.getcwd() + '\\src\\files_storage\\images\\info\\'
    photo_name = [name for name in os.listdir(photo_path) if 'photo' in name]
    photo_path += photo_name[0] 
    return photo_path


def retrieve_resume():
    resume_path = os.getcwd() + '\\src\\files_storage\\resume\\'
    resume_name = [name for name in os.listdir(resume_path) if 'resume' in name]
    resume_path += resume_name[0] 
    return resume_path


def remove_cover():
    cover_path = os.getcwd() + '\\src\\files_storage\\images\\info\\'
    cover_name = [name for name in os.listdir(cover_path) if 'cover' in name]
    os.remove(cover_path + cover_name[0])


def remove_photo():
    photo_path = os.getcwd() + '\\src\\files_storage\\images\\info\\'
    photo_name = [name for name in os.listdir(photo_path) if 'photo' in name]
    os.remove(photo_path + photo_name[0])


def remove_resume():
    resume_path = os.getcwd() + '\\src\\files_storage\\resume\\'
    resume_name = [name for name in os.listdir(resume_path) if 'resume' in name]
    os.remove(resume_path + resume_name[0])