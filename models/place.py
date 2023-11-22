#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.review import Review

if storage_type == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 nullable=False)
                          )


    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", backref="place", cascade="all, delete-orphans")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

else:
    class Place(BaseModel):
        """place to stay"""
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            all_reviews = list(storage.all(Review).values())
            return list(filter(lambda c: c.place_id == self.id, all_reviews))

        @property
        def amenities(self):
            all_amenities = list(storage.all(Amenity).values())
            return list(filter(lambda a: a.id == self.amenity_ids, all_amenities))

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(Amenity.id)
