#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    su = 0

    for i in range(1, len(sys.argv)):
        su = int(sys.argv[i]) + su

    print(su)
