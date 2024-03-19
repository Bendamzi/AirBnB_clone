#!/usr/bin/env python3
"""This module contains the state class definition"""

import sys
import os

sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
except Exception as e:
    print(e)


class State(BaseModel):
    """This is the class for State object"""
    name = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()
        else:
            super().__init__(**kwargs)
