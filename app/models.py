# -*- coding: utf-8 -*-

import json
from datetime import datetime
from .extensions import db


class Message(db.Model):
    """
    Message model
    """
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    title = db.Column(db.String(32), unique=True, nullable=False)
    body = db.Column(db.String(512), nullable=False)
