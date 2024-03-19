#!/usr/bin/env python3
""" This module houses a set of test cases for the Review class"""

import os
import sys
import unittest


sys.path.append(os.getcwd())
try:
    from models.review import Review
except Exception as e:
    print(e)


class TestReviewModel(unittest.TestCase):
    """This test class collects a series of tests for the class Review"""

    def test_init_method_for_Review(self):
        """This method tests the attribute of an
        instance of Review class"""
        my_review = Review()
        self.assertTrue(len(my_review.id) > 0)

    def test_instance_of_the_id(self):
        """This tests the instance of the id"""
        my_review = Review()
        self.assertIsInstance(my_review.id, str)

    def test_init_method_for_review_with_dict_data(self):
        """This tests the instance of the .to_dict method"""
        my_review = Review()
        my_review.text = "my review"
        dict_review = my_review.to_dict()
        self.assertIsInstance(dict_review, dict)

    def test_str_method(self):
        """This method test the str magic function"""
        my_review = Review()
        review_str = str(my_review)
        review_exp_str = "[{}] ({}) {}".format(
                                        my_review.__class__.__name__,
                                        my_review.id, my_review.__dict__)
        self.assertEqual(review_str, review_exp_str)
