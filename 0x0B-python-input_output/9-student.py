#!/usr/bin/python3
"""Ä module containing a class"""


class Student:
    """Ä class with instances"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ä method that retrieves a dictionary
        representation of a Student instance"""
        return self.__dict__
