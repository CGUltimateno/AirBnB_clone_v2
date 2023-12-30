#!/usr/bin/python3
"""
Module for the Place class
"""
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                        Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """
    The Place class from which future Place objects will be derived
    """
    __tablename__ = 'places'
    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          default=0,
                          nullable=False)
    number_bathrooms = Column(Integer,
                              default=0,
                              nullable=False)
    max_guest = Column(Integer,
                       default=0,
                       nullable=False)
    price_by_night = Column(Integer,
                            default=0,
                            nullable=False)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    amenity_ids = []

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',
                               backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        @property
        def reviews(self):
            """
            Getter attribute in case of file storage
            """
            from models import storage
            from models.review import Review

            reviews = []
            all_reviews = storage.all(Review)

            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews.append(review)

            return reviews
