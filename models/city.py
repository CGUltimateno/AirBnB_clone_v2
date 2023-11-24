#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv

from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        state_id = Column(ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)

        places = relationship("Place", backref="cities",
                              cascade="all,delete-orphan")
    else:
        state_id = ""
        name = ""
