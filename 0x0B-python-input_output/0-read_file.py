#!/usr/bin/python3
"""Define function that read files"""


def read_file(filename=""):
    """Reading file using 'with'"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
