# -*- coding: utf-8 -*-

from flask_restplus import Namespace, Resource
from ..serializers.auth import auth_response
from ..parsers import auth_parser

ns = Namespace('auth', description='Auth related operations')


# ================================================================================================
# ENDPOINTS
# ================================================================================================
#
#   API auth endpoints
#
# ================================================================================================

@ns.route('/')
class TokenGenerator(Resource):

    @ns.marshal_with(auth_response)
    @ns.expect(auth_parser)
    def post(self):
        """
        Token generation
        """
        data = auth_parser.parse_args()

        return {'success': True}
