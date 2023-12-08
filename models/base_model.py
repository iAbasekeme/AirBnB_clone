#!/usr/bin/python3
"""This file contains a super class BaseModel
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """A BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """An init method for instances
        """
        if kwargs:
            del kwargs['__class__']
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.strptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """A string method

        Returns:
                str: For string output
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """A save method to update time
        """
        self.updated_at = datetime.now()
        storage.save()

        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance

        Returns:
                dict: dictionary for all instances
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))

print("-----------------------")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
