#!/usr/bin/python3
""""Module contaning an empty class"""


class BaseGeometry:
    """A class contaning two fucntions"""

    def integer_validator(self, name, value):
        """Funcion that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def are(self):
        """Ä function that raises an exception"""
        raise Exception("area() is not implemented")
