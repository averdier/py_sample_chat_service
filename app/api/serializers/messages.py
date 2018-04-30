# -*- coding: utf-8 -*-

from flask_restplus import fields
from .. import api


message_post_model = api.model('Message POST model', {
    'title': fields.String(required=True, min_length=3, max_length=32),
    'body': fields.String(required=True, max_length=512)
})

message_put_model = api.inherit('Message PUT model', message_post_model, {})

message_patch_model = api.model('Message PATCH model', {
    'title': fields.String(required=False, min_length=3, max_length=32),
    'body': fields.String(required=False, max_length=512)
})

message_resource_model = api.model('Message resource model', {
    'id': fields.Integer(required=True),
    'created_at': fields.DateTime(dt_format='iso8601', required=True),
    'updated_at': fields.DateTime(dt_format='iso8601', required=True),
    'title': fields.String(required=True)
})

message_model = api.inherit('Message model', message_resource_model, {
    'body': fields.String(required=True)
})

messages_container = api.model('Messages container', {
    'messages': fields.List(fields.Nested(message_resource_model), required=True)
})
