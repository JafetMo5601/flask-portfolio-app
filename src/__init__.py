from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pymongo import MongoClient
from flask import Flask
import argparse


db = None
app = None


def create_api(config):
    global db
    global app

    app = Flask(__name__)
    app.config.from_object(config)

    JWTManager(app)
    db = SQLAlchemy(app)

    from src.blueprints.admin import admin_bp
    app.register_blueprint(admin_bp)
    from src.blueprints.auth import auth_bp
    app.register_blueprint(auth_bp)
    from src.blueprints.info import info_bp
    app.register_blueprint(info_bp)

    from src import models

    return app


def parse_args():
    parser = argparse.ArgumentParser(description='Portfolio')
    parser.add_argument(
        '--enable-prod',
        action='store_true',
        default=False,
        help='Flag for production deployment. Warning: This will disable debugging mode.'
    )
    return parser.parse_args()
