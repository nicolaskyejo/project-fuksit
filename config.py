import os
import redis
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    """Base config variables"""
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SESSION_TYPE = os.getenv('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(os.getenv('SESSION_REDIS'))


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True
    TESTING = True

    SQLALCHEMY_ECHO =  True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
