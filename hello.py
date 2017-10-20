#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:00:51 2017

@author: root
"""
            
x = 3
ans = 0
intersleft = x
while (intersleft != 0):
        ans = ans + x
        intersleft = intersleft - 1
print (str(x), '*', str(x) ,'=', str(ans))

'''tESTING SORTING ALGORITHM'''
L = [['a',1], ['a',2], ['a',3], ['b',1], ['b',2], ['b',3]]
L.sort(key=lambda k: (k[0], -k[1]), reverse=True)
print(L)

file = [21,33,21,332,12,-12,33,33,452,321,644,30,0]
#file.sort(key=None, reverse=False)
file.sort()
print(file)
        