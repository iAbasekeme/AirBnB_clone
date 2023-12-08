#!/usr/bin/python3
"""This file contains a super class BaseModel
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """A BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """An init method for instances
        """
        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.strptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f'))
                elif k != '__class__':
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
