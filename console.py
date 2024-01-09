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
        """Creates a new instance of a valid class,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel"""
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

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $show BaseModel 1234-1234-1234.
        """
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        all_objects = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in all_objects:
            str_to_show = str(all_objects[key])
            print(str_to_show)
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
