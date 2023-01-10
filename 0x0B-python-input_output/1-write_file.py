#!/usr/bin/python3
"""Ä module containing a function that writes a string"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        char_written = f.write(text)
    return char_written
