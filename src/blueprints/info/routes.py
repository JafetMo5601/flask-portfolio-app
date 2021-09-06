from flask_jwt_extended import jwt_required
from flask import jsonify, request

from src.blueprints.info import info
from . import info_bp


@info_bp.route('/add-info/', methods=['POST'])
def add_info():
    about = request.json['about']
    description = request.json['description']
    resume = request.json['resume']
    phone = request.json['phone']
    email = request.json['email']
    direction = request.json['direction']
    linkedin = request.json['linkedin']
    gh = request.json['github']
    insta = request.json['instagram']
    fb = request.json['facebook']

    response = info.add_info(
        about, description, resume, phone, email, direction, linkedin, gh, insta, fb)

    return jsonify(response=response[0]), response[1]


@info_bp.route('/info/', methods=['GET'])
def user_info():
    response = info.get_info()
    return jsonify(response=response[0]), response[1]


@info_bp.route('/update-info/<int:id>/', methods=['PUT'])
def update_info(id):
    about = request.json['about']
    description = request.json['description']
    resume = request.json['resume']
    phone = request.json['phone']
    email = request.json['email']
    direction = request.json['direction']
    linkedin = request.json['linkedin']
    gh = request.json['github']
    insta = request.json['instagram']
    fb = request.json['facebook']

    response = info.update_info(
        id, about, description, resume, phone, email, direction, linkedin, gh, insta, fb)
    return jsonify(response=response[0]), response[1]


@info_bp.route('/remove-info/<int:id>/', methods=['DELETE'])
def remove_info(id):
    response = info.remove_info(id)
    return jsonify(response=response[0]), response[1]


@info_bp.route('/add-project/', methods=['POST'])
def add_project():
    title = request.json['title']
    description = request.json['description']
    tools = request.json['tools']
    image = request.json['image']
    response = info.add_project(title, description, tools, image)
    return jsonify(response=response[0]), response[1]


@info_bp.route('/projects/', methods=['GET'])
def user_projects():
    response = info.get_projects()
    return jsonify(response=response[0]), response[1]


@info_bp.route('/remove-project/<int:id>/', methods=['DELETE'])
def remove_project(id):
    response = info.remove_project(id)
    return jsonify(response=response[0]), response[1]


@info_bp.route('/update-project/<int:id>/', methods=['PUT'])
def update_project(id):
    title = request.json['title']
    description = request.json['description']
    tools = request.json['tools']
    image = request.json['image']
    response = info.update_project(id, title, description, tools, image)
    return jsonify(response=response[0]), response[1]


@info_bp.route('/add-award/', methods=['POST'])
def add_award():
    title = request.json['title']
    description = request.json['description']
    response = info.add_award(title, description)
    return jsonify(response=response[0]), response[1]


@info_bp.route('/awards/', methods=['GET'])
def user_awards():
    response = info.get_awards()
    return jsonify(response=response[0]), response[1]


@info_bp.route('/remove-award/<int:id>/', methods=['DELETE'])
def remove_award(id):
    response = info.remove_award(id)
    return jsonify(response=response[0]), response[1]


@info_bp.route('/update-award/<int:id>/', methods=['PUT'])
def update_award(id):
    title = request.json['title']
    description = request.json['description']
    response = info.update_award(id, title, description)
    return jsonify(response=response[0]), response[1]
