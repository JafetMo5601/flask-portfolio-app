from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
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
