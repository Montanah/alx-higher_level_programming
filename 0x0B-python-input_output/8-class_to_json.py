#!/usr/bin/python3
"""module with dictionary-creation function"""


def class_to_json(obj):
    """a function that returns the dictionary description"""
    return obj.__dict__
