#!/usr/bin/python3
"""module containing a rectangle class which inherits from rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class which inherits from rectangle"""

    def __init__(self, size):
        """initializes a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
