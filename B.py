# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:29:17 2023

@author: ASUS
"""

def multiply_elements_for(input_list):
    result_list = []
    for element in input_list:
        result_list.append(element * 2)
    return result_list

numbers_list = [1, 2, 3, 4, 5]
result_for = multiply_elements_for(numbers_list)
print(result_for)




def multiply_elements_list_comprehension(input_list):
    return [element * 2 for element in input_list]

numbers_list = [1, 2, 3, 4, 5]
result_list_comprehension = multiply_elements_list_comprehension(numbers_list)
print(result_list_comprehension)