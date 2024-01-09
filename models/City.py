#!/usr/bin/python3
"""City class inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """two Public class attributes city.id and name"""

    state_id = ""
    name = ""
