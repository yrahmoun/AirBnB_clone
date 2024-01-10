#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd
import shlex
import json
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

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
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
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.
        Ex: $ all BaseModel or $ all.
        """

        storage.reload()
        result_list = []
        all_objects = storage.all()

        if not arg:
            for key in all_objects:
                result_list.append(str(all_objects[key]))
            print(json.dumps(result_list))
            return

        token = shlex.split(arg)
        if token[0] in HBNBCommand.valid_classes.keys():
            for key in all_objects:
                if token[0] in key:
                    result_list.append(str(all_objects[key]))
            print(json.dumps(result_list))
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
