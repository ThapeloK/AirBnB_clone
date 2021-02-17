#!/usr/bin/python3
"""This contains the storage file"""

import json
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.review import Review

class Filestorage():
"""serializing and deserializing instances"""
__file_path = "file.json"
__objects = {}

def all(self):
    """returns objects"""
    return self.__objects

def new(self, obj):
    """set key in objects"""
    if obj is not None:
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

        def save(self):
            """serializing objects with json"""
            json_objects = {}
            for key in self.__objects:
                json_objects[key] = self.__objects[key].to_dict()
                with open(self.__file_path, "w") as myFile:
                    json.dump(json_objects, myFile)

                    def reload(self):

