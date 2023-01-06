#!/usr/bin/python3
import sys
size = len(sys.argv)
if size <= 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(size))
for i in range(1, size):
    print("{}: {}".format(i, sys.argv[i]))
