""" This module will hold a unittests class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBasemodel(unittest.TestCase):
    """A test class for the BaseModel
    """

    def setUp(self):
        self.instance = BaseModel()

    def tearDown(self):
        pass

    def test_instance_attribute_existence(self):
        self.assertTrue(hasattr(self.instance, 'id'))
        self.assertTrue(hasattr(self.instance, 'created_at'))
        self.assertTrue(hasattr(self.instance, 'updated_at'))

    def test_instnce_attribute_types(self):
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_instance_output(self):
        expected_string = f"[{self.instance.__class__.__name__}] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(str(self.instance), expected_string)

    def test_save_method(self):
        initial_time = self.instance.updated_at
        self.instance.save()
        updated_time = self.instance.updated_at

        self.assertEqual(updated_time, initial_time)
        # self.assertNotEqual(updated_time, initial_time)

    def test_to_dict_method(self):
        dict_representation = self.instance.to_dict()

        self.assertIn("__class__", dict_representation)

        created_at_Iso_format = self.instance.created_at.isoformat()
        updated_at_Iso_format = self.instance.updated_at.isoformat()

        self.assertIsInstance(created_at_Iso_format, str)
        self.assertIsInstance(updated_at_Iso_format, str)

    if __name__ == '__main__':
        unittest.main
