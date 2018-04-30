# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint,
          title='Message service',
          version='1.0',
          description='Python sample message service',
          )

from .endpoints.postman import ns as postman_namespace
from .endpoints.messages import ns as messages_namespace

api.add_namespace(postman_namespace)
api.add_namespace(messages_namespace)
