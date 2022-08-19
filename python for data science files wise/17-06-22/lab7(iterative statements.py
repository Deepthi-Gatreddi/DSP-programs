# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 17:28:47 2022

@author: DEEPTHI
iterative statements
"""
for i in range(1,6):
    print(i)
for i in range(10,1,-1):
    print(i)
i=1
while(i<=10):
    print(i)
    i=i+1
j=10
while(j>=1):
    print(j) 
    j=j-1   
for i in range(1,10):
    print(i)
for i in range(10,1):
    print(i)
for i in 10:
    print(i)
for i in range(5):
    print(i)
str="I am deepthi"
for i in str:
    print(i)
lis=[1,5,2]
for i in lis:
    print(lis)
for i in lis:
    print(i)
#printing sum of numbers
n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print(sum)
#factorial of numbers
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print(fact)