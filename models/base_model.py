#!/usr/bin/python3
""" defines the BaseModel class """
import uuid
from datetime import datetime


class BaseModel:
    """the base class for the project"""

    def __init__(self, *args, **kwargs):
        """intializes a new instance of the clas"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == '__class__':
                    continue
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return a string representation of BaseModel instance"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """changes the updated_at attribute"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """converts the BaseModel instance to a dictionary"""
        dct = {**self.__dict__}
        dct['__class__'] = type(self).__name__
        dct['created_at'] = dct['created_at'].isoformat()
        dct['updated_at'] = dct['updated_at'].isoformat()
        return dct
