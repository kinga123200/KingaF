# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:25:23 2023

@author: ASUS
"""

def check_sum_greater_or_equal(a: int, b: int, c: int) -> bool:
    return (a + b) >= c

num1 = 5
num2 = 8
num3 = 12
result = check_sum_greater_or_equal(num1, num2, num3)

print(result)
