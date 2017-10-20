#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:25:51 2017

@author: root
"""

largest = None

for i in range(1, 11):
    number = int(input('Enter integer #%d: ' % i))
    if number % 2 != 0 and (not largest or number > largest):
        largest = number

if largest is None:
    print ("You didn't enter any odd numbers")
else:
    print ("Your largest odd number was:", largest)