#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:51:17 2017

@author: root
"""

num = 20
for test in range(num):
    if test%2 ==0:
        if test%3 ==0:
            sqr = test * test
            print('----------------------------------------------')
            print("|test is divisible by 2 amd 3", test, '|', 'squre is', sqr, '|')
            print('----------------------------------------------')
        else:
            print("it is divisible by 2 and not 3")
            
    else:
        print("it is not divisible by 2")