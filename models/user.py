#!/usr/bin/python3
"""User class inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Public class attributes : email,password,first_name,last_name"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
