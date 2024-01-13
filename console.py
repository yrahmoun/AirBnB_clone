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
from datetime import datetime


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

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
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
        if len(tokens) <= 2:
            print("** attribute name missing **")
            return
        if len(tokens) <= 3:
            print("** value missing **")
            return
        all_objects = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key not in all_objects:
            print("** no instance found **")
            return
        attr_name = tokens[2]
        attr_value = tokens[3]
        instance = all_objects[key]
        if attr_name in ("id", "updated_at", "created_at"):
            return
        if attr_name in instance.__dict__:
            attr_type = type(instance.__dict__[attr_name])
            instance.__dict__[attr_name] = attr_type(attr_value)
        else:
            instance.__dict__[attr_name] = attr_value
        instance.updated_at = datetime.utcnow()
        instance.save()

    def do_count(self, arg):
        """
        Counts the instances of a specific class.
        """
        instance_count = 0
        all_objects = storage.all()

        for obj_key in all_objects:
            if arg in obj_key:
                instance_count += 1

        print(instance_count)

    def default(self, arg):
        """Handle new ways of inputting data"""
        val_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }

        arg = arg.strip()
        values = arg.split(".")
        if len(values) != 2:
            cmd.Cmd.default(self, arg)
            return

        class_name = values[0]
        command = values[1].split("(")[0]
        line = ""

        if command == "update" and values[1].endswith("}"):
            # If it's an "update" command with a dictionary input
            inputs = values[1].split("(")[1].rsplit(",", 1)
            attribute_name = shlex.split(inputs[0])[0]
            attribute_value = inputs[1].strip()[:-1]
            line = f"{class_name} {values[1].split('(')[0]} {attribute_name} \"{attribute_value}\""
            self.do_update(line.strip())
            return

        try:
            inputs = values[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if num != len(inputs) - 1:
                    line += f" {shlex.split(inputs[num])[0]}"
                else:
                    line += f" {shlex.split(inputs[num][0:-1])[0]}"
        except IndexError:
            inputs = ""
            line = ""

        line = f"{class_name}{line}"

        if command in val_dict:
            val_dict[command](line.strip())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
