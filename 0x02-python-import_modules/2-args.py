#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 arguments:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(size))
    for i in range(1, size):
        print("{}: {}".format(i, argv[i]))
