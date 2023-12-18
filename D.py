# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:29:53 2023

@author: ASUS
"""



def display_every_second_element(numbers):
    for i in range(1, len(numbers), 2):
        print(numbers[i])

numbers_list = list(range(116, 211))  
display_every_second_element(numbers_list)