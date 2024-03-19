#!/usr/bin/env python3
""" This module houses a set of test cases for the User class"""


import os
import sys
import unittest
from datetime import datetime


sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
    from models.user import User
except Exception as e:
    print(e)


class TestUserModel(unittest.TestCase):
    """This test class collects a series of tests for the class BaseModel"""

    def test_init_method_for_user(self):
        """This method tests the attribute of an
        instance of BaseModel class"""
        my_user = User()
        self.assertTrue(len(my_user.id) > 0 and isinstance(my_user.id, str))
        self.assertTrue(isinstance(my_user.created_at, datetime))
        self.assertTrue(isinstance(my_user.updated_at, datetime))

    def test_init_method_for_user_with_dict_data(self):
        """This tests the initialization, with a given dictionary
        data, handled by **kwargs"""
        my_user = User()
        my_user.first_name = "ALX"
        my_user.last_name = "Betty"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        dict_user = my_user.to_dict()
        my_user2 = User(**dict_user)
        self.assertFalse(my_user == my_user2)
        self.assertEqual(my_user.id, my_user2.id)
        self.assertEqual(my_user.created_at, my_user2.created_at)
        self.assertEqual(my_user.updated_at, my_user2.updated_at)
        self.assertTrue(my_user.first_name == my_user2.first_name)
        self.assertTrue(my_user.last_name == my_user2.last_name)

    def test_str_method(self):
        """This method test the str magic function"""
        my_user = User()
        user_str = str(my_user)
        user_exp_str = "[{}] ({}) {}".format(my_user.__class__.__name__,
                                             my_user.id, my_user.__dict__)
        self.assertEqual(user_str, user_exp_str)

    def test_save_method(self):
        """This method tests the value of the attribute
        that is updated by the save method"""
        my_user = User()
        updated_at_before = my_user.updated_at
        my_user.save()
        self.assertNotEqual(updated_at_before, my_user.updated_at)
        self.assertTrue(isinstance(my_user.updated_at, datetime))
        self.assertTrue(isinstance(updated_at_before, datetime))

    def test_to_dict_method(self):
        """This method validates the logic of the
        to_dict method via testing"""
        my_user = User()
        self.assertFalse("__class__" in my_user.__dict__)
        my_user_dict = my_user.to_dict()
        self.assertTrue("__class__" in my_user_dict)
