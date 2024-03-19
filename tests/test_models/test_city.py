#!/usr/bin/env python3
""" This module houses a set of test cases for the City class"""


import os
import sys
import unittest


sys.path.append(os.getcwd())
try:
    from models.city import City
except Exception as e:
    print(e)


class TestCityModel(unittest.TestCase):
    """This test class collects a series of tests for the class BaseModel"""

    def test_init_method_for_city(self):
        """This method tests the attribute of an
        instance of City class"""
        my_city = City()
        self.assertTrue(len(my_city.id) > 0)

    def test_instance_of_the_id(self):
        """This tests the instance of the id"""
        my_city = City()
        self.assertIsInstance(my_city.id, str)

    def test_init_method_for_city_with_dict_data(self):
        """This tests the instance of the .to_dict method"""
        my_city = City()
        my_city.name = "Balcony"
        dict_city = my_city.to_dict()
        self.assertIsInstance(dict_city, dict)

    def test_str_method(self):
        """This method test the str magic function"""
        my_city = City()
        city_str = str(my_city)
        city_exp_str = "[{}] ({}) {}".format(
                                      my_city.__class__.__name__,
                                      my_city.id, my_city.__dict__)
        self.assertEqual(city_str, city_exp_str)
