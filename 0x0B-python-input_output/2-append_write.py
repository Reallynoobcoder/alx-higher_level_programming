#!/usr/bin/python3
"""Define function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appen string into a file using 'with'"""
    with open(filename, 'a') as file:
        return file.write(text)
