#!/usr/bin/env python3
"""This module contains the Amenity class definition"""

import sys
import os

sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
except Exception as e:
    print(e)


class Amenity(BaseModel):
    """This is the class for Amenity object"""

    name = ""

    def __init__(self, *args, **kwargs):
        """This method initializes an instance of this class"""
        if len(kwargs) == 0:
            super().__init__()
        elif len(kwargs) > 0:
            super().__init__(**kwargs)
