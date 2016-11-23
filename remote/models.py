# -*- coding: utf-8 -*-

from sqlalchemy import Column, Unicode, Integer
from sqlalchemy.ext.declarative import declarative_base

Models = declarative_base()

class Channel(Models):
    __tablename__ = 'channels'

    pk = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False, unique=True)
    stream = Column(Unicode, nullable=False)
    url = Column(Unicode, nullable=True)
    logo = Column(Unicode, nullable=True)
    feed = Column(Unicode, nullable=True)
