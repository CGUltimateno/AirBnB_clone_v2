#!/usr/bin/python3
"""
Module for the Amenity class
"""
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """
    The Amenity class from which future Amenity objects will be derived
    """
    tablename = "amenities"

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
