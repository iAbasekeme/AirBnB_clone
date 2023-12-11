""" This module will hold a unittests class
"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """A test class for the BaseModel
    """

    def setUp(self):
        self.BaseModel = BaseModel()

    def tearDown(self):
        pass
    if __name__ == '__main__':
        unittest.main
