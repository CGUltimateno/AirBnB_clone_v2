#!/usr/bin/python3
"""
Module for the City class
"""
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """
    The City class from which future City objects will be derived
    """
    name = ""
    state_id = ""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ""
        state_id = ""
