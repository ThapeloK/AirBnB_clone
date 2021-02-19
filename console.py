#!/usr/bin/python3
"""This contains the console"""

import models
import cmd
import re
import shlex
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review
from models.base_model import BaseModel
from models import storage 


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
