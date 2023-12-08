#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method that return the dictionary
        """
        return self.__objects

    def new(self,obj):
        """
        Method that construct our dictionay with key(class.id)
        and value(obj==>{})
        """
        #dict = {334HF4, 2023 12 7 11 5 454,2023 12 7 11 5 487} 
        #__dict= {key: {}}
        #key = name_class.id
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialization of the dictionary to JSON file
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        save = json.dumps(new_dict)
        with open(self.__file_path, "w") as file:
            file.write(save)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
