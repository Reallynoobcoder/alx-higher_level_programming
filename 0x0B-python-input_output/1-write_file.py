#!/usr/bin/python3
"""Define function that write into a files"""


def write_file(filename="", text=""):
    """writing into a file using 'with'"""
    with open(filename, 'w') as file:
        return file.write(text)
