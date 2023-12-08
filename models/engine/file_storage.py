"""A class for file storage
"""
import json
import sys
import models
print(sys.path)


class FileStorage:
    """A class filestorage for file storage
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
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump({key: value.to_dict for key,
                       value in FileStorage.__objects.items()}, file)

    def reload(self):
        if self.__file_path:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        else:
            pass
