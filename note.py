#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:07:09 2017

@author: root
"""

count = 0
s = 'nbob is a bbob  man bbob'
s = s.split()
#for i in range (0, len(s)):
for i in range (0, len(s)):
    if s[i] == 'bob':
        count += 1
print("Number of times bob occurs is: "+str(count))