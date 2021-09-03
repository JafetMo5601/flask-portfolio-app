from flask import jsonify, request
from flask_jwt_extended import create_access_token

from src import get_collection
from . import auth_bp


@auth_bp.route('/register/', methods=['POST'])
def register():
    email = request.json['email']
    is_email_registered = get_collection('users').find_one({'email': email})

    if is_email_registered:
        return jsonify(message='This email already registered'), 409
    else:
        first = request.json['first']
        last = request.json['last']
        password = request.json['password']
        user_info = dict(first=first,
                         last=last, email=email, password=password)

        get_collection('users').insert_one(user_info)

        return jsonify(message='User registered sucessfully'), 201


@auth_bp.route('/login/', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']

    is_user_valid = get_collection('users').find_one(
        {'email': email, 'password': password})

    if is_user_valid:
        access_token = create_access_token(identity=email)
        return jsonify(message='Login Succeeded!', access_token=access_token), 201
    else:
        return jsonify(message='Bad Email or Password'), 401
