#!/usr/bin/python3
"""Module containing a class that can raise an exception and validate a
 value"""


class BaseGeometry:
    """A class that can raise an exception and validate a value"""

    def integer_validator(self, name, value):
        """Function that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """A function that raises an exception"""
        raise Exception("area() is not implemented")
