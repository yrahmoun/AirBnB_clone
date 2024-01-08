#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ executes commands """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ exit the program """
        print("")
        return True

    def emptyline(self):
        """ does nothing """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
