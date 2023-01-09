#!/usr/bin/python3
""""Module contaning an empty class"""


class BaseGeometry:
    """A class contaning a fucntion gets the area"""
    def area(self):
        """A function that can raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Funcion that validates value"""
        if isinstance(value, int) not True:
            TypeError("{} must be an integer".format(name))
        if value <= 0:
            ValueError("<name> must be greater than 0")
