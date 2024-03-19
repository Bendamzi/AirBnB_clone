#!/usr/bin/env python3
"""This module contains the definition for amenity class"""

import sys
import os

sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
except Exception as e:
    print(e)


class Place(BaseModel):
    """This is the class definition for the amenity object"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []

    def __init__(self, *args, **kwargs):
        """This method initializes an object of this class"""
        if len(kwargs) == 0:
            super().__init__()
        elif len(kwargs) > 0:
            super().__init__(**kwargs)
