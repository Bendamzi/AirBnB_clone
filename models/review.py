#!/usr/bin/env python3
"""This module handles the definition of the review class"""

import sys
import os

sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
except Exception as e:
    print(e)


class Review(BaseModel):
    """This is the class definition for Reviwe object"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """This method initialized an object of this class"""
        if len(kwargs) == 0:
            super().__init__()
        elif len(kwargs) > 0:
            super().__init__(**kwargs)
