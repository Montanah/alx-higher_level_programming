#!/usr/bin/python3
"""A molue with a JSON function"""

import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file"""
    with open(filename, 'r') as f:
        my_obj = json.load(f)
    return my_obj
