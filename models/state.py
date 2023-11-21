#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """Gets the cities of the current state"""
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
