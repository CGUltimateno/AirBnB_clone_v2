#!/usr/bin/python3
"""
Module for the user class
"""
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel):
    """
    The user class from which future user objects will be derived
    """
    __tablename__ = 'users'
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128),
                       nullable=False)
        password = Column(String(128),
                          nullable=False)
        first_name = Column(String(128),
                            nullable=True)
        last_name = Column(String(128),
                           nullable=True)
        places = relationship('Place',
                              backref='user',
                              cascade='all, delete')
        reviews = relationship('Review',
                               backref='user',
                               cascade='all, delete')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
