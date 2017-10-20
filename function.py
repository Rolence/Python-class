#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:32:45 2017

@author: root
"""

def changeme(str):
    #str = "this sdifs sdnfsif sdfjs"
    print (str)
    return;

changeme(str)
changeme("this na first")
changeme("this na second")

##Pass by reference
#!/usr/bin/python

# Function definition is here
def changeme1( mylist ):
   "This changes a passed list into this function"
   #mylist.append([1,2,3,4]);
   mylist = [1,2,3,4]
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme1( mylist );
print ("Values outside the function: ", mylist)

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )


# Function definition is here
def printinfo1( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo1( age=50, name="miki" )
printinfo1( name="miki" )

# Lamda Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))


# Return Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print ("Outside the function : ", total )