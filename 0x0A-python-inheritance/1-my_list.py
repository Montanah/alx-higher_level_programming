#!/usr/bin/python3
""" Module that contains a list subclass """


class MyList(list):
    """ Subclass containing sorted list """
    def print_sorted(self):
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
        del sorted_list
