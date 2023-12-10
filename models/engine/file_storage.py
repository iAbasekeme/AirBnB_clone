#!/usr/bin/python3
"""
FileStorage module
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns all the objects
        """
        return self.__objects

    def new(self, obj):
        """This method creates a object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump({key: value.to_dict() for key,
                       value in FileStorage.__objects.items()}, file)

    def reload(self):
        """
        Method for deserialization of the dictionnary
        """
        try:
            # os.path.exists(FileStorage.__file_path)
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                # print("hereee")
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    obj = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
