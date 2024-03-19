#!/usr/bin/env python3
""" This module houses a set of test cases for the State class"""

import os
import sys
import unittest


sys.path.append(os.getcwd())
try:
    from models.state import State
except Exception as e:
    print(e)


class TestStateModel(unittest.TestCase):
    """This test class collects a series of tests for the class State"""

    def test_init_method_for_state(self):
        """This method tests the attribute of an
        instance of State class"""
        my_state = State()
        self.assertTrue(len(my_state.id) > 0)

    def test_instance_of_the_id(self):
        """This tests the instance of the id"""
        my_state = State()
        self.assertIsInstance(my_state.id, str)

    def test_init_method_for_state_with_dict_data(self):
        """This tests the instance of the .to_dict method"""
        my_state = State()
        my_state.name = "Lagos, Nigeria"
        dict_state = my_state.to_dict()
        self.assertIsInstance(dict_state, dict)

    def test_str_method(self):
        """This method test the str magic function"""
        my_state = State()
        state_str = str(my_state)
        state_exp_str = "[{}] ({}) {}".format(
                                       my_state.__class__.__name__,
                                       my_state.id, my_state.__dict__)
        self.assertEqual(state_str, state_exp_str)
