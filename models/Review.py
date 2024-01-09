#!/usr/bin/python3
""" Review class inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes : Place.id, User.id, text"""

    place_id = ""
    user_id = ""
    text = ""
