#!/usr/bin/python3
"""
Module for the State class
"""
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from os import environ

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    The State class from which future State objects will be derived
    """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False)
    cities = relationship('City',
                          backref='state',
                          cascade='all, delete')

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter for cities attribute
            """
            from models import storage
            from models.city import City

            city_list = []
            for key, value in storage.all(City).items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
