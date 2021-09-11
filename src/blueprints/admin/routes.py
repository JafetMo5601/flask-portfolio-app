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
    cover_img = request.files['cover'] if (request.files.get('cover')) else ''
    photo_img = request.files['photo'] if (request.files.get('photo')) else ''
    resume_file = request.files['resume'] if (request.files.get('resume')) else ''
    phone = request.form['phone']
    email = request.form['email']
    direction = request.form['direction']
    linkedin = request.form['linkedin']
    gh = request.form['github']
    insta = request.form['instagram']
    fb = request.form['facebook']
    response = admin.add_info(
        about, description, cover_img, photo_img, resume_file, phone, email, direction, linkedin, gh, insta, fb)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/update-info/', methods=['PUT'])
@jwt_required()
def update_info():
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
    response = admin.update_info(about, description, cover, photo,
                                 resume, phone, email, direction, linkedin, gh, insta, fb)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/remove-info/', methods=['DELETE'])
@jwt_required()
def remove_info():
    response = admin.remove_info()
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/add-project/', methods=['POST'])
@jwt_required()
def add_project():
    title = request.form['title']
    description = request.form['description']
    tools = request.form['tools']
    image = request.files['image'] if (request.files.get('image')) else ''
    response = admin.add_project(title, description, tools, image)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/update-project/<int:id>/', methods=['PUT'])
@jwt_required()
def update_project(id):
    title = request.form['title']
    description = request.form['description']
    tools = request.form['tools']
    image = request.files['image']
    response = admin.update_project(id, title, description, tools, image)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/remove-project/<int:id>/', methods=['DELETE'])
@jwt_required()
def remove_project(id):
    response = admin.remove_project(id)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/add-award/', methods=['POST'])
@jwt_required()
def add_award():
    title = request.json['title']
    description = request.json['description']
    year = request.json['year']
    response = admin.add_award(title, description, year)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/update-award/<int:id>/', methods=['PUT'])
@jwt_required()
def update_award(id):
    title = request.json['title']
    description = request.json['description']
    response = admin.update_award(id, title, description)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/remove-award/<int:id>/', methods=['DELETE'])
@jwt_required()
def remove_award(id):
    response = admin.remove_award(id)
    return jsonify(response=response[0]), response[1]


@admin_bp.route('/add-award-cover/', methods=['POST'])
@jwt_required()
def add_award_cover():
    image = request.files['award-image']
    response = admin.add_award_cover(image)
    return jsonify(response=response[0]), response[1]
