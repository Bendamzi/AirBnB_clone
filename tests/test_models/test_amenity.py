#!/usr/bin/env python3
""" This module houses a set of test cases for the Amenity class"""


import os
import sys
import unittest


sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
    from models.amenity import Amenity
except Exception as e:
    print(e)


class TestAmenityModel(unittest.TestCase):
    """This test class collects a series of tests for the class BaseModel"""

    def test_init_method_for_amenity(self):
        """This method tests the attribute of an
        instance of Amenity class"""
        my_amenity = Amenity()
        self.assertTrue(len(my_amenity.id) > 0)

    def test_instance_of_the_id(self):
        """This tests the instance od the id"""
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity.id, str)

    def test_init_method_for_amenity_with_dict_data(self):
        """This tests the instance of the .to_dict method"""
        my_amenity = Amenity()
        my_amenity.name = "Balcony"
        dict_amenity = my_amenity.to_dict()
        self.assertIsInstance(dict_amenity, dict)

    def test_str_method(self):
        """This method test the str magic function"""
        my_amenity = Amenity()
        amenity_str = str(my_amenity)
        amenity_exp_str = "[{}] ({}) {}".format(
                                        my_amenity.__class__.__name__,
                                        my_amenity.id, my_amenity.__dict__)
        self.assertEqual(amenity_str, amenity_exp_str)
