#!/usr/bin/python3
"""Module contaning a class"""


class BaseGeometry:
    """A class contaning two functions"""

    def integer_validator(self, name, value):
        """Function that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """Ä function that raises an exception"""
        raise Exception("area() is not implemented")
