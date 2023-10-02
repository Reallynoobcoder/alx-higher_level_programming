#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return ""
        result = ["#" * self.__width] * self.__height
        return '\n'.join(result)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        lis = []
        for i in range(self.__height):
            for j in range(self.__width):
                lis.append(str(self.print_symbol))
            if i != self.__height - 1:
                lis.append("\n")
        return "".join(lis)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
