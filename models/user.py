#!/usr/bin/python3
"""This class will e handling a user class
"""
from base_model import BaseModel


class User(BaseModel):
    emiail = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        super().__init__(self, *args, **kwargs):
            pass