# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:28:28 2023

@author: ASUS
"""


def process_lists_and_return_result(list1, list2):
    combined_list = list1 + list2

    unique_list = list(set(combined_list))

    cubed_list = [x ** 3 for x in unique_list]

    return cubed_list

list_a = [1, 2, 3]
list_b = [3, 4, 5]
result_list = process_lists_and_return_result(list_a, list_b)

print(result_list)

