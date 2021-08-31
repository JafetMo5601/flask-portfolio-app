from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from flask import Flask
import argparse


def connection():
    # client = MongoClient('mongodb://' + os.environ.get('PORTFOLIO_DB_HOST') + ':27017/')
    client = MongoClient('mongodb://localhost:27017/')
    
    db = client['portfolio']    
    return db


def get_collection(collection_name):
    user = connection()[collection_name]
    return user


def create_api(config):
    app = Flask(__name__)
    JWTManager(app)
    
    app.config.from_object(config)
    
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