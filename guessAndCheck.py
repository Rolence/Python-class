#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:51:47 2017

@author: root
"""

ans = 0
num = int(input("enter an integer: "))
while ans ** 3 < abs(num):
    ans = ans + 1
if ans**3 != abs(num):
    print(num, " is not a perfect cube")
    
else:
    print( num, " is a perfect cube")