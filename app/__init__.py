# -*- coding: utf-8 -*-

from flask import Flask
from config import config
from .extensions import db


def create_app(config_name='default'):
    """
    Create Flask app
    :param config_name:
    :return: Flask
    """

    from .api import blueprint as api_blueprint

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    app.register_blueprint(api_blueprint)

    extensions(app)

    with app.app_context():
        from app.models import Message

        #db.drop_all()
        db.create_all()

    return app


def extensions(app):
    """
    Init extensions
    """
    db.init_app(app)