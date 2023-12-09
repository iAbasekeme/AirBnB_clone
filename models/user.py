#!/usr/bin/python3
"""
user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class will e handling a user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
