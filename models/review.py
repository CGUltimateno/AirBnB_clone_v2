#!/usr/bin/python3
"""
Module for the Review class
"""
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """
    The Review class from which future Review objects will be derived
    """
    __tablename__ = 'reviews'
    text = Column(String(1024),
                  nullable=False)
    place_id = Column(String(60),
                      ForeignKey('places.id'),
                      nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)

