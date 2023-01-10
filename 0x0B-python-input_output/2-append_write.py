#!/usr/bin/python3
"""A module with a fucntion that appends as string"""


def append_write(filename="", text=""):
    """Ä function that appends a string at the end of a text file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        chars_read = f.write(text)
    return chars_read
