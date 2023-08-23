#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ 
    Review class to store review information 
    Attributes:
        __tablename__ (str): The name of the table in the database.
        place_id (str): The foreign key referencing the id of the place associated with the review.
        user_id (str): The foreign key referencing the id of the user who wrote the review.
        text (str): The text content of the review.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("places.id"), nullable=False) 
    text = Column(String(1024), nullable=False)
