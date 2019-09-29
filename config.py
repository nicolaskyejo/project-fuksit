import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    """Base config variables"""
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SESSION_COOKIE_NAME =


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    # DATABASE_URI =


class DevConfig(Config):
    DEBUG = True
    TESTING = True
    # DATABASE_URI
