#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    for item in set(my_list):
        sum = sum + item
    return sum
