#!/usr/bin/python3
"""This contains the console"""

import cmd
import models
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review
from models.base_model import BaseModel

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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

    def create(self, arg):
        """creating a new class instance"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            print((arg[0])().id)
            storage.save()

    def show(self, arg):
        """string rep of an instance based on class name and id"""
        o_dic = storage.all
        if len(arg) == 0:
            print("* class name missing *")
            return False
        elif arg[0] not in classes:
            print("* class doesn't exist *")
            return False
        elif len(arg) == 1:
            print("* instance id missing **")
            return False
        elif "{}.{}".format(arg[0], arg[1]) not in o_dic:
            print("** no instance found **")
            return False
        else:
            print(o_dic["{}.{}".format(arg1[0], arg1[1])])

    def destroy(self, arg):
        """deletion of an instance based on class name and id"""
        o_dic = storage.all
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in o_dic.keys():
            print("** no instance found **")
        else:
            del o_dic["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def all(self, arg):
        """string representation of all instances"""
        if len(arg) > 0 and arg[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj = []
            for ob in storage.all().values():
                if len(arg) > 0 and arg[0] == obj.__class__.__name__:
                    obj.append(ob.__str__())
                elif len(arg) == 0:
                    obj.append(ob.__str__())
                    print(obj)

    def update(self, arg):
        """update instances based on class name and id"""
        o_dic = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        if arg[0] not in classes:
            print("** class doesn't exist **")
        if len(arg) == 1:
            print("** instance id missing **")
        if "{}.{}".format(argl[0], argl[1]) not in o_dic.keys():
            print("** no instance found **")
        if len(arg) == 2:
            print("** attribute name missing **")
        storage.save()


def parse(arg):
    """mapping (tuple conversion)"""
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
