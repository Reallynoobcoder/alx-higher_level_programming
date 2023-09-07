#!/usr/bin/python3
import sys

leng = len(sys.argv)

if leng == 1:
    leng = leng - 1
    print("{} arguments.".format(leng))
else:
    print("{} arguments:".format(leng))

for i in range(1, leng):
    print("{}: {}".format(i, leng))
