import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    SECRET_KEY = 'P0rtf0l10@pp'
    # SECRET_KEY = os.environ.get('PORTFOLIO_SECRET_KEY') # P0rtf0l10@pp


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False