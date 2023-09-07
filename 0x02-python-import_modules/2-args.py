#!/usr/bin/python3
import sys

leng = len(sys.argv)

if leng == 1:
    print("{} argument{}.".format(leng - 1, '' if leng == 2 else 's'))
else:
    print("{} arguments:".format(leng - 1))

for i in range(1, leng):
    print("{}: {}".format(i, sys.argv[i]))
