# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:36:37 2019

@author: CEC
"""
def fib1(n):
    a, b = 0,1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print("")

