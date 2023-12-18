# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 18:41:25 2023

@author: ASUS
"""
def create_greeting(name: str, surname: str) -> str:
    greeting = "Cześć {} {}".format(name, surname)
    return greeting

name = "Kinga"
surname = "Kowalska"
result = create_greeting(name, surname)

print(result)
