#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    lst1 = [k * v for k, v in my_list]
    lst2 = [v for k, v in my_list]

    sum_lst1 = 0
    sum_lst2 = 0
    for item1, item2 in zip(lst1, lst2):
        sum_lst1 = sum_lst1 + item1
        sum_lst2 = sum_lst2 + item2
    return sum_lst1/sum_lst2
