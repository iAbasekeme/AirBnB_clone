#!/usr/bin/python3
"""
FileStorage module
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method that return the dictionnary containing attributes
        """
        return self.__objects

    def new(self, obj):
        """
        Method that add a key as class_name.id with the value to the dictionary
        """
        key = obj.__class__.__name__ + "." + obj.id  # Ex = BaseModel.12121212
        self.__objects[key] = obj

    def save(self):
        """
        Method for serialization of the dictionnary
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        save = json.dumps(new_dict)

        with open(self.__file_path, "w") as file:
            file.write(save)

    def reload(self):
        """
        Method for deserialization of the dictionnary
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
