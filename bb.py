# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:32:55 2023

@author: ASUS
"""

def display_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

numbers_list = list(range(116, 211))
display_even_numbers(numbers_list)

