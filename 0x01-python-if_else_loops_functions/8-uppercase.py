#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
            print(upper_char, end="")
        else:
            print(char, end="")
    print()
