#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd
import shlex
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """executes commands"""

    prompt = "(hbnb) "
    valid_classes = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Review": Review,
        "State": State,
        "Place": Place,
        "User": User,
    }

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        print("")
        return True

    def emptyline(self):
        """does nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of valid classes"""
        if not arg:
            print("** class name missing **")
            return
        cls_to_create = shlex.split(arg)
        if cls_to_create[0] not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        instance = HBNBCommand.valid_classes[cls_to_create[0]]()
        instance.save()
        print(instance.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
