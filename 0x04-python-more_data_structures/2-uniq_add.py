#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_numbers = set()
    for i in my_list:
        if i not in uniq_numbers:
            uniq_numbers.add(i)
    return ((sum(uniq_numbers)))
