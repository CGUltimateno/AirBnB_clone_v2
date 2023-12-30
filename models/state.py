#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""
        cities = ""

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
            @property
            def cities(self):
                """getter attribute cities that returns the list of City instances
                with state_id equals to the current State.id"""
                cities = []
                for city in models.storage.all(City).values():
                    if city.state_id == self.id:
                        cities.append(city)
                return cities
