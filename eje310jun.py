# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:06:09 2022

@author: Alumno
"""

def suma(*a):
    print("\ntipo de datos del argumento:",
         type(a))
    sum=0
    for n in a:
        sum+= n
    print("suma:", sum)
    
suma(3)
suma(1)
suma(3,5)