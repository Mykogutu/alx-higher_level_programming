#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_total = 0
    total_weight = 0
    for score, weight in my_list:
        weight_total += score * weight
        total_weight += weight
    return weight_total / total_weight
