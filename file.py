#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:45:40 2017

@author: root
"""
# Open a file
'''
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("mode of the file: ", fo.mode)
print ("Name of the file: ", fo.closed)

# Close opend file
fo.close()
print ("Name of the file: ", fo.closed)
'''

# Open a file
str = input('Enter the content of the file: ')
#fo = open("foo.txt", "w")
fo = open("foo.txt", "a+")
#fo.write( "Python is a great language.\nYeah its great!!\n",str);
fo.write( str);
# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read();
print ("Read String is : ", str)
# Close opend file
fo.close()