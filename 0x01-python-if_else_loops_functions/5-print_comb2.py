#!/usr/bin/python3
for num in range(0, 100):
    print("{}{}".format(int(num / 10), int(num % 10)), end="")
    if (num < 99):
        print(", ", end="")
