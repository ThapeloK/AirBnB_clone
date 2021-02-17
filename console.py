#!/usr/bin/python3
"""This contains the console"""

import models
import cmd
import shlex
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB command interpretor"""
    prompt = "(hbnb) "

    def emptyline(self):
        """if empty do nothing"""
        return False

    def do_quit(self, arg):
        """exit program using quit command"""
        return True

    def do_EOF(self, arg):
        """exit program using EOF"""
        return True

    def do_create(self, arg):
        """create a new class instance"""
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in classes:            print("** class doesn't exist **")
            return False
        print(newInstance.id)
        newInstance.save()

        def do_show(self, arg):
            """string rep of an instance based on class name and id"""
            if len(args) == 0:
                print("** class name missing **")
                return False
            elif args[0] not in classes:
                print("** class doesn't exist **")
                return False
            elif len(args) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1] not in objdict:
                  print("** no instance found **")
                    else:
                    print(objdict["{}.{}".format(args[0], args[1])])

        def do_destroy(self, arg):
        """deletion of an instance based on class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
        print("** class name is missing **")
        return False
        elif args[0] not in classes:
        print("** no instance found **")
        else:
        print("** instance id missing **")
        else:
        print("** class doesn't exist **")

        def do_all(self, arg)
        """string representation of all instances"""
        args = shlex.split(arg)
