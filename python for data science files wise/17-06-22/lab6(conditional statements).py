# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 09:18:52 2022

@author: DEEPTHI
conditional statements
printing maximam number among three numbers
"""
#using simple if
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
if(a>=b and a>=c):
    print("max term is",a)
if(b>=a and b>=c):
    print("max term is",b)
if(c>=a and c>=b):
    print(c)
#another way using simple if with less complexity
max=a
if(b>max):
     max=b
if(c>max):
    max=c
print("maximum number is",max)
    
#using if else
if(a>=b and a>=c):
    print(a,"is maximam")
else:
    if(b>c):
        print(b,"is maximum")
    else:
        print(c,"is maximum")
#using else if 
if(a>=b and a>=c):
    print("max valueis",a)
elif(b>c):
    print("max value is",b)
else:
    print("max value is",c)
#checking given number is positive or not
m=int(input("enter a value"))
if(m>0):
    print(m,"is positive")
elif(m<0):
    print(m,"is negitive")
else:
    print(m,"is equals to 0")