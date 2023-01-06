#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    total = 0

    if size <= 1:
        total = 0
    else:
        for i in range(1, size):
            total = total + int(sys.argv[i])
        print(total)
