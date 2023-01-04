#!/usr/bin/python3
"""A module contaning a square class"""


class Square:
    """Class representing a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Method initialzing a square of size size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """method that returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """method that sets the position of the square"""
        if isinstance(value, tuple) is False or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Mtethod that returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Method prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return
        for a in range((self.__position)[1]):
            print()
        for i in range(self.__size):
            for b in range((self.__position)[0]):
                print(' ', end='')
            for j in range(self.size):
                print("#", end='')
            print()
