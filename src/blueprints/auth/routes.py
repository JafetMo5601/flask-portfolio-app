from flask import jsonify, request
from flask_jwt_extended import create_access_token

from src.blueprints.auth import auth
from . import auth_bp


@auth_bp.route('/register/', methods=['POST'])
def register():
    email = request.json['email']

    if auth.is_email_registered(email):
        return jsonify(response = 'Conflict.', message = 'Email already registered'), 409
    else:
        first = request.json['first']
        last = request.json['last']
        password = request.json['password']
        auth.is_email_registered(first, last, email, password)
        return jsonify(response = 'Created.', message='User registered sucessfully'), 201


@auth_bp.route('/login/', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    if auth.are_credentials_valid(email, password):
        JWT = create_access_token(identity=email)
        return jsonify(response = 'Ok.', message = 'Login Succeeded!', JWT = JWT), 200
    else:
        return jsonify(response = 'Unauthorized.', message='Bad Email or Password'), 401
