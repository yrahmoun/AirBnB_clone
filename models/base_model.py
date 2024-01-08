#!/usr/bin/python3
""" defines the BaseModel class """
import uuid
from datetime import datetime


class BaseModel:
    """ the base class for the project """

    def __init__(self):
        """ intializes a new instance of the clas """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """ return a string representation of BaseModel instance """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """ changes the updated_at attribute """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ converts the BaseModel instance to a dictionary """
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
