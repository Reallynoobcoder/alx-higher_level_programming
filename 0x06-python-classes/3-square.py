#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Define method size of square"""
    def __init__(self, size=0):
        """initialization of a new square

        size is the size of new aquare
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return area of the square"""
        return (self.__size ** 2)
