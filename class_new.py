#!/usr/bin/python

'''class Employee:
    empcount = 0

    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
        Employee.empcount += 1


    def display(self):
        print "Total emp is %d" %Employee.empcount

    def details(self):
        print "Name: ",self.name ,  "pay: ",self.pay


emp1 = Employee("poo",200)
emp2 = Employee("soo",300)

emp1.display()
emp1.details()'''

var1 = raw_input("Enter the first string: ")
var2 = raw_input("Enter the second string: ")

if len(var1) != len(var2):
    print "sorry string doesn't match"
else:
    count = 0
    while count < len(var1):
        if var1[count] in var2:
            count +=1
        else:
            print "False"
    print "True"        
        
    
