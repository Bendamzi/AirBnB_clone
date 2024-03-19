#!/usr/bin/env python3
""" This module houses a set of test cases for the Place class"""

import os
import sys
import unittest


sys.path.append(os.getcwd())
try:
    from models.place import Place
except Exception as e:
    print(e)


class TestPlaceModel(unittest.TestCase):
    """This test class collects a series of tests for the class Place"""

    def test_init_method_for_place(self):
        """This method tests the attribute of an
        instance of Place class"""
        my_place = Place()
        self.assertTrue(len(my_place.id) > 0)

    def test_instance_of_the_id(self):
        """This tests the instance of the id"""
        my_place = Place()
        self.assertIsInstance(my_place.id, str)

    def test_init_method_for_place_with_dict_data(self):
        """This tests the instance of the .to_dict method"""
        my_place = Place()
        my_place.name = "Lagos, Nigeria"
        dict_place = my_place.to_dict()
        self.assertIsInstance(dict_place, dict)

    def test_str_method(self):
        """This method test the str magic function"""
        my_place = Place()
        place_str = str(my_place)
        place_exp_str = "[{}] ({}) {}".format(
                                       my_place.__class__.__name__,
                                       my_place.id, my_place.__dict__)
        self.assertEqual(place_str, place_exp_str)
