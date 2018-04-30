# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base configuration
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    RESTPLUS_MASK_SWAGGER = False

    SECRET_KEY = '<YOU_KEY>'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configuration
    """
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}