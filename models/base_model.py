#!/usr/bin/python3
"""This file contains a super class BaseModel
"""
import uuid
from datetime import datetime

class BaseModel:
    """A BaseModel class
    """
    def __init__(self):        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):        
        self.updated_at = datetime.now()        
        
        
    def to_dict(self):                   
        return {k: v for k, v in self.__dict__.items()}
    
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print('---------------------------------------')
my_model.save()
print(my_model)
print('---------------------------------------')
my_model_json = my_model.to_dict()
print(my_model_json)
print('---------------------------------------')

print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))