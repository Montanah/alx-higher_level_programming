#!/usr/bin/python3
''' module containing rectangle class '''


class Rectangle:
    ''' rectangle class with width, height, area, and perimeter '''
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError('height must be integer')
        if value < 0:
            raise ValueErroe('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        string = ''
        for row in range(self.__height):
            for col in range(self.__width):
                string = string + '#'
            string = string + '\n'
        return string[:-1]

    def __repr__(self):
        return 'Rectangle('+str(self.__width)+', '+str(self.__height)+')'
