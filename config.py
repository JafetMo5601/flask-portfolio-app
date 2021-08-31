import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    SECRET_KEY = os.environ.get('PORTFOLIO_SECRET_KEY') 
    FLASK_SECRET = SECRET_KEY
    JWT_SECRET_KEY = SECRET_KEY
    DB_HOST = os.environ.get('PORTFOLIO_DB_HOST')


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProdConfig(Config):
    DEBUG = False
    DEVELOPMENT = False