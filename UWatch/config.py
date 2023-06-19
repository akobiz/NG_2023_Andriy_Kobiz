from os import path
from commands import generateVideoURL

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    DEBUG = False
    SECRET_KEY = generateVideoURL()[:15]
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uwatch.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MODELS_IMPORT_PATH = 'models'
    UPLOAD_FOLDER = 'static/uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
