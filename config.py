# coding: utf-8
from abc import ABC

class Config(ABC):
    SECRET_KEY = 'secret'

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:secret@localhost/statusok_cursos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing(Config):
    pass

config = {
    'development': Development,
    'testing': Testing
}