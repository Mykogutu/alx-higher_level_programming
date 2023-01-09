#!/usr/bin/python3
if __name__ == "__main__":
    def print_reversed_list_integer(my_list=[]):
        new_reversed = my_list[::-1]
        for i in new_reversed:
            print("{}".format(i))
