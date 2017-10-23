#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:44:28 2017

@author: root
"""
class Company:
    staffCount = 0
    departmentCount = 0
    def __init__(self, name, income, expenditure, departments):
        self.name = name
        self.income = income
        self.expenditure = expenditure
        self.departments = departments
        Company.staffCount +=1
        Company.departmentCount +=1
        
    def comName(self):
        print ("Company name is: ", self.name)
        
    def displayComp(self):
        print("Company name: ",self.name, "Income",self.income,"Expences",self.expenditure,"department",self.departments)
comp = Company("Skylabase", 1234567,123456,"CommuFi")
comp.displayComp()
print ("totsl nimber of departments %d" % Company.departmentCount,"total number of employees: %d"% Company.staffCount)        

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
      
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)