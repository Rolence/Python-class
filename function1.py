#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:44:25 2017

@author: root
"""

total = 0; # This is global variable.
# Function definition is here
def sum( num1, num2 ):
   # Add both the parameters and return them."
   num1 = 12
   num2 = 23
   total = num1 + num2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
total =sum( 10, 20 );
print ("Outside the function global total : ", total )