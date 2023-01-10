#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_reversed = my_list[::-1]
    for i in new_reversed:
        print("{:d}".format(i))
