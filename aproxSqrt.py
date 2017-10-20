#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:55:49 2017

@author: root
"""
#approximation of square root
x = 25
x = int(input("enter the number to find the approximated square root: "))
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print ('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print ('Failed on square root of', x)
else:
    print (ans, 'is close to square root of', x)