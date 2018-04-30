# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_httpauth import HTTPTokenAuth
from flask_restplus import Api

authorizations = {
    'tokenKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

blueprint = Blueprint('bearer', __name__, url_prefix='/bearer')
api = Api(blueprint,
          title='Sample API',
          version='1',
          description='Python sample API protected with Bearer token',
          authorizations=authorizations,
          security='tokenKey'
          )

auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    """
    Verify authorization token

    :param token:
    :return:
    """
    if token == '1DB1D3CF2FC65':
        return True

    return False


from .endpoints.messages import ns as messages_namespace

api.add_namespace(messages_namespace)
