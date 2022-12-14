#!/usr/bin/python3
"""A module containing one function"""


def read_file(filename=""):
    """A function that reads file and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
