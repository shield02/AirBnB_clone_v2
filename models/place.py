#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.review import Review
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy import Integer, String, relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="delete")
    else:
        def reviews(self):
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    amenity_ids = []
