#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_delete = [key for key in a_dictionary if a_dictionary[key] == value]
    for key in key_to_delete:
        del a_dictionary[key]
