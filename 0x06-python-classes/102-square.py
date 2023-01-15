#!/usr/bin/python3
"""A module contaning a square class"""


class Square:
    """Class representing a square"""
    def __init__(self, size=0):
        """Method initialzing a square of size size"""

        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.size = size

    def __lt__(self, other):
        """method for <"""
        if self.__size < other.__size:
            return True
        else:
            return False

    def __le__(self, other):
        """method for <="""

        if self.__size <= other.__size:
            return True
        else:
            return False

    def __gt__(self, other):
        """method for >"""
        if self.__size > other.__size:
            return True
        else:
            return False

    def __ge__(self, other):
        """method for >="""
        if self.__size >= other.__size:
            return True
        else:
            return False

    def __eq__(self, other):
        """method for =="""
        if self.__size == other.__size:
            return True
        else:
            return False

    def __ne__(self, other):
        """method for !="""
        if self.__size != other.__size:
            return True
        else:
            return False

    @property
    def size(self):
        """Method that returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets the size of the square"""
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Mtethod that returns the area of the square"""
        return self.__size * self.__size
