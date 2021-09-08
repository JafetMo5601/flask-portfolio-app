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
    return response


@info_bp.route('/cover/', methods=['GET'])
def user_cover():
    response = info.get_cover()
    return response


@info_bp.route('/photo/', methods=['GET'])
def user_photo():
    response = info.get_photo()
    return response