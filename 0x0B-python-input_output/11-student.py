#!/usr/bin/python3
"""Ä module containing a class"""


class Student:
    """Ä class with instances"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ä method that retrieves a dictionary
        representation of a Student instance"""
        if isinstance(attrs, list) is True:
            my_dict = dict()
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__[key]
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """changes attributes of the object"""
        for key in self.__dict__:
            if key in json:
                self.__dict__[key] = json[key]
