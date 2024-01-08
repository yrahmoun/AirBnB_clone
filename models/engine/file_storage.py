#!/usr/bin/python3
""" defines the class FileStorage """

import json
import os
from models.base_model import BaseModel


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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        serialized_objects = {
                key: value.to_dict()
                for key, value in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(serialized_objects))

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    class_instance = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = class_instance
