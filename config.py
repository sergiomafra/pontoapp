from dotenv import load_dotenv

import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
DOTENV_PATH = os.path.join(BASEDIR, '.env')
load_dotenv(DOTENV_PATH)

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['PONTOAPP_SECRET_KEY'].rstrip('\n')
    SQLALCHEMY_DATABASE_URI = os.getenv('PONTOAPP_DATABASE_URL').rstrip('\n')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
