import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    SECRET_KEY = os.environ.get('PORTFOLIO_SECRET_KEY') 
    FLASK_SECRET = SECRET_KEY
    JWT_SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = os.getcwd() + '\\src\\files_storage\\'

class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    

class ProdConfig(Config):
    DEBUG = False
    DEVELOPMENT = False