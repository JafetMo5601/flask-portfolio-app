from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import argparse


db = SQLAlchemy()


def create_api(config):
    app = Flask(__name__)
    JWTManager(app)

    app.config.from_object(config)
    db.init_app(app)    
    migrate = Migrate(app, db)
    
    from src.models import models
    
    from src.blueprints.admin import admin_bp
    app.register_blueprint(admin_bp)
    
    from src.blueprints.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    from src.blueprints.info import info_bp
    app.register_blueprint(info_bp)

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