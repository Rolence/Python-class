#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:43:54 2017

@author: root
"""
'''
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

num = 10
while num > 3:
    num -= 1
    print(num) 


num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

num =0
i=0
while i < 5:
    num +=2
    print(num)
    i +=1
print("Goodbye")'''

i = 0
end = 6
add = 0
while i <= end:
    add =add +i
    
    i+=1
    
print (add)