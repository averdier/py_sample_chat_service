# -*- coding: utf-8 -*-

from flask_restplus import fields
from .. import api


auth_response = api.model('Auth response', {
    'success': fields.Boolean(required=True)
})
