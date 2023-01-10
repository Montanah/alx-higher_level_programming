#!/usr/bin/python3
"""A module that contains a json function"""

import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string"""
    return json.loads(my_str)
