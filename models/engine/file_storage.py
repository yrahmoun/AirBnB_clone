#!/usr/bin/python3
""" defines the class FileStorage """

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """ serializes instances to a JSON file
    and deserializes JSON file to instance """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ stores obj with key <obj class name>.id in __objects """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        serialized_objects = {
                key: value.to_dict()
                for key, value in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    data = json.load(f)
                    for key, obj_dict in data.items():
                        class_name, obj_id = key.split('.')
                        class_instance = eval(class_name)(**obj_dict)
                        FileStorage.__objects[key] = class_instance
                except Exception:
                    pass
