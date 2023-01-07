#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size = len(argv)
    if size == 1:
        print("0 arguments.")
    elif size == 2:
        print("1 argument.")
        print("1: {}".format(argv[1]))
    elif size > 2:
        print("{} arguments:".format(size - 1))
        for i in range(1, size):
            print("{}: {}".format(i, argv[i]))
