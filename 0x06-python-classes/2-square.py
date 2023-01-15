#!/usr/bin/python3
"""A module contaning a square class"""


class Square:
    """Class representing a square"""
    def __init__(self, size=0):
        """Method initializing a square of size size"""

        if isinstance(size, int) is False:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size
