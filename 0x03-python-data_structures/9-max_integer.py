#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    max_n = 0
    for i in my_list:
        if my_list[i] > max_n:
            max_n = my_list[i]
        return (max_n)
