#!/usr/bin/python
def no_c(my_string):
    new_str = ""
    for s in my_string:
        if s != "C" and s != "c":
            new_str += s
    return (new_str)
