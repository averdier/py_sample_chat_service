# -*- coding: utf-8 -*-

from flask import request
from flask_restplus import Namespace, Resource, abort
from ..serializers.messages import messages_container, message_post_model, message_model, message_patch_model, message_put_model
from app.extensions import db
from app.models import Message

ns = Namespace('messages', description='Messages related operations.')


# ================================================================================================
# ENDPOINTS
# ================================================================================================
#
#   API messages endpoints
#
# ================================================================================================


@ns.route('/')
class MessageCollection(Resource):

    @ns.marshal_with(messages_container)
    def get(self):
        """
        Return messages
        """
        return {'messages': [m for m in Message.query.all()]}

    @ns.marshal_with(message_model)
    @ns.expect(message_post_model)
    def post(self):
        """
        Add message
        """
        data = request.json

        if Message.query.filter_by(title=data['title']).first() is not None:
            abort(400, error='Title already exist')

        m = Message(
            title=data['title'],
            body=data['body']
        )

        db.session.add(m)
        db.session.commit()

        return m


@ns.route('/<id>')
@ns.response(404, 'Message not found.')
class MessageItem(Resource):

    @ns.marshal_with(message_model)
    def get(self, id):
        """
        Return message
        """
        return Message.query.get_or_404(id)

    @ns.marshal_with(message_model)
    @ns.expect(message_put_model)
    def put(self, id):
        """
        Update full message
        """
        m = Message.query.get_or_404(id)
        data = request.json

        m_search = Message.query.filter_by(title=data['title']).first()
        if m_search is not None and m_search.id != m.id:
            abort(400, error='Title already exist')

        m.title = data['title']
        m.body = data['body']

        db.session.add(m)
        db.session.commit()

        return m

    @ns.marshal_with(message_model)
    @ns.expect(message_patch_model)
    def patch(self, id):
        """
        Update message
        """
        m = Message.query.get_or_404(id)
        data = request.json

        if not len(data):
            abort(400, error='No data found.')

        if data.get('title'):
            m_search = Message.query.filter_by(title=data['title']).first()
            if m_search is not None and m_search.id != m.id:
                abort(400, error='Title already exist')

            m.title = data['title']

        if data.get('body'):
            m.body = data['body']

        db.session.add(m)
        db.session.commit()

        return m

    @ns.response(204, 'Message successfully deleted.')
    def delete(self, id):
        """
        Delete message
        """
        m = Message.query.get_or_404(id)

        db.session.delete(m)
        db.session.commit()

        return 'Message successfully deleted.', 204
