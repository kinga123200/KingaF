# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:28:09 2023

@author: ASUS
"""

def check_value_in_list(lst: list, value: int) -> bool:
    return value in lst

my_list = [1, 3, 5, 7, 9]
search_value = 7
result = check_value_in_list(my_list, search_value)

print(result)
