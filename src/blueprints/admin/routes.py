from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
from flask import jsonify, request

from src.blueprints.admin import admin
from . import admin_bp
    
    
@admin_bp.route('/add-info/', methods=['POST'])
@jwt_required()
def add_info():
    about = request.form['about']
    description = request.form['description']
    cover = request.files['cover'] if (request.files.get('cover')) else ''
    photo = request.files['photo'] if (request.files.get('photo')) else ''
    resume = request.files['resume'] if (request.files.get('resume')) else ''
    phone = request.form['phone']
    email = request.form['email']
    direction = request.form['direction']
    linkedin = request.form['linkedin']
    gh = request.form['github']
    insta = request.form['instagram']
    fb = request.form['facebook']

    cover_path = admin.save_image(cover)
    photo_path = admin.save_image(photo, True)
    resume_path = admin.save_resume(resume)
    
    response = admin.add_info(
        about, description, cover_path, photo_path, resume_path, phone, email, direction, linkedin, gh, insta, fb)

    return jsonify(response=response[0]), response[1]


@admin_bp.route('/update-info/<int:id>/', methods=['PUT'])
@jwt_required()
def update_info(id):
    about = request.form['about']
    description = request.form['description']
    cover = request.files['cover'] if (request.files.get('cover')) else ''
    photo = request.files['photo'] if (request.files.get('photo')) else ''
    resume = request.files['resume'] if (request.files.get('resume')) else ''
    phone = request.form['phone']
    email = request.form['email']
    direction = request.form['direction']
    linkedin = request.form['linkedin']
    gh = request.form['github']
    insta = request.form['instagram']
    fb = request.form['facebook']
    
    cover = admin.retrieve_cover() if (cover == '') else admin.save_image(cover)
    photo = admin.retrieve_photo() if (photo == '') else admin.save_image(photo, True)
    resume = admin.retrieve_resume() if (resume == '') else admin.save_resume(resume)

    response = admin.update_info(
        id, about, description, cover, photo, resume, phone, email, direction, linkedin, gh, insta, fb)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/remove-info/<int:id>/', methods=['DELETE'])
@jwt_required()
def remove_info(id):
    response = admin.remove_info(id)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/add-project/', methods=['POST'])
@jwt_required()
def add_project():
    title = request.json['title']
    description = request.json['description']
    tools = request.json['tools']
    image = request.json['image'] if (request.files.get('image')) else ''
    response = admin.add_project(title, description, tools, image)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/remove-project/<int:id>/', methods=['DELETE'])
@jwt_required()
def remove_project(id):
    response = admin.remove_project(id)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/update-project/<int:id>/', methods=['PUT'])
@jwt_required()
def update_project(id):
    title = request.json['title']
    description = request.json['description']
    tools = request.json['tools']
    image = request.json['image']
    response = admin.update_project(id, title, description, tools, image)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/add-award/', methods=['POST'])
@jwt_required()
def add_award():
    title = request.json['title']
    description = request.json['description']
    response = admin.add_award(title, description)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/remove-award/<int:id>/', methods=['DELETE'])
@jwt_required()
def remove_award(id):
    response = admin.remove_award(id)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/update-award/<int:id>/', methods=['PUT'])
@jwt_required()
def update_award(id):
    title = request.json['title']
    description = request.json['description']
    response = admin.update_award(id, title, description)
    return jsonify(response=response[0]), response[1]