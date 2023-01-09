#!/usr/bin/python3
""""Module contaning an empty class"""


class BaseGeometry:
    """A class contaning two fucntions"""

    def integer_validator(self, name, value):
        """Funcion that validates value"""
        if isinstance(value, int) not True:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

    def are(self):
        """Ä fucntion that raises an exception"""
        raise Exception("area() is not implemented")
