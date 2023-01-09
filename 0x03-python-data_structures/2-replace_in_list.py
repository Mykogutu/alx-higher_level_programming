#!/usr/bin/python3i
if __name__ == "__main__":
    def replace_in_list(my_list, idx, element):
        if idx < 1:
            return(my_list)
        elif idx > len(my_list):
            return(my_list)
        else:
            my_list[idx] = element
            return(my_list)
