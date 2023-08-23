#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.review import Review
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy import Integer, String, Table
from sqlalchemy.orm import relationship


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

    # For DBStorage
    reviews = relationship("Review", backref="place", cascade="delete")

    # For FileStorage
    def get_reviews(self):
        """
        Returns the list of Review instances with place_id equals to the current Place.id
        """
        return self.reviews.filter(Review.place_id == self.id)

    amenity_ids = []

    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False,
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False,
        ),
    )

    # For DBStorage
    amenities = relationship("Amenity", secondary="place_amenity", backref="place_amenities", viewonly=False)

    # For FileStorage
    def amenities(self):
        """getter attribute returns the list of Amenity instances"""
        from models.amenity import Amenity
        amenity_list = []
        all_amenities = models.storage.all(Amenity)
        for amenity in all_amenities.values():
            if amenity.place_id == self.id:
                amenity_list.append(amenity)
        return amenity_list

