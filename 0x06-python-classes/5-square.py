#!/usr/bin/python3
"""A module contaning a square class"""


class Square:
    """Class representing a square"""
    def __init__(self, size=0):
        """Method initialzing a square of size size"""
        self.size = size

    @property
    def size(self):
        """Method that returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets the size of the square"""
        if isinstance(value, int) is not True:
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Mtethod that returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Method prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.size):
                print("#", end='')
            print()
