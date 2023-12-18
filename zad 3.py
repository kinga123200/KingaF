# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:24:21 2023

@author: ASUS
"""

def is_even(number: int) -> bool:
    return number % 2 == 0

given_number = 10
result = is_even(given_number)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
    