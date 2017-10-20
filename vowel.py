#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:15:13 2017

@author: root
"""
'''
data = input("Please type a sentence: ")
vowels = "aeiou"
for v in vowels:
    vow = sum(data.lower().count(v))
    
    #print (sum(vow))
    print (v, data.lower().count(v))
print (vow)'''

count = 0
word = 'bob'
s = "azcbobobEgghakl"
s12 = input("Please type a sentence: ")
#s = s.lower()
'''for i in range(0, len(s)):
    if s[i] == 'a'or s[i] == 'e'or s[i] == 'i'or s[i] == 'o'or s[i] == 'u':
        count += 1
print("Number of vowels: "+str(count))'''
s1 = "azcbobobEgghakl"
s1 = s1.split()
for i in range (0, len(s1)):
    if s1[i] == 'bob':
        count += 1
print("Number of bobs: "+str(count))