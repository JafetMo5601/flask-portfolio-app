from flask import jsonify, request, current_app

from src.blueprints.info import info
from . import info_bp


@info_bp.route('/info/', methods=['GET'])
def user_info():
    response = info.get_info()
    return jsonify(response=response[0]), response[1]


@info_bp.route('/projects/', methods=['GET'])
def user_projects():
    response = info.get_projects()
    return jsonify(response=response[0]), response[1]


@info_bp.route('/awards/', methods=['GET'])
def user_awards():
    response = info.get_awards()
    return jsonify(response=response[0]), response[1]


@info_bp.route('/resume/', methods=['GET'])
def user_resume():
    response = info.get_resume()
    return jsonify(response[0]), response[1]


@info_bp.route('/retrieve-image/', methods=['GET'])
def project_image():
    image_name =  request.json['image_name']
    image_type =  request.json['image_type']
    response = info.get_image(image_name, image_type)
    return response[0], response[1]