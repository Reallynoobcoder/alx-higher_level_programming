#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    for string in dir():
        if string[0:2] != '__':
            print(string)
