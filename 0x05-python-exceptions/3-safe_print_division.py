#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        pp = a / b
    except ZeroDivisionError:
        pp = None
    finally:
        print("Inside result: {}".format(pp))
    return pp
