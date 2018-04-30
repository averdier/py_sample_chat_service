# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from flask_restplus import Api

authorizations = {
    'basicAuth': {
        'type': 'basic',
        'in': 'header'
    }
}

blueprint = Blueprint('basic', __name__, url_prefix='/basic')
api = Api(blueprint,
          title='Sample API',
          version='1',
          description='Python sample API protected with Basic Auth',
          authorizations=authorizations,
          security='basicAuth'
          )

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """
    Verify Device authorization

    :param username: Device uuid
    :type username: str
    :param password: Device key
    :type password: str

    :return: True if device can connect, else False
    :rtype: bool
    """

    if username == 'elonet' and password == 'elonet':
        return True

    return False

from .endpoints.messages import ns as messages_namespace

api.add_namespace(messages_namespace)
