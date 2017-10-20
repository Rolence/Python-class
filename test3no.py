#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:08:59 2017

@author: root
"""
import math
name = 'agege'
print (3*name)
num1 = int(input('enter first number'))
num2 = int(input('enter second number'))
num3 = int(input("enter third number"))
if num1 < num2 and num1 < num3:
    if num1%2 != 0:
        print ('num1 is leaast and odd')
    
    else:
        print ('num1 is leaast but even')
elif num2 < num3:
        if num2%2 !=0:
            print ('num2 is leaast and odd')
            
        else:
            print('num2 is least but even')
else:
    print('num3 is least and odd')