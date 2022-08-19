# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 18:03:32 2022

@author: DEEPTHI
functions
"""
#simple function
def Display():
    print("Hello world")
Display()

#factorial of a num
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter a Number:"))
m=fact(n)
print("factorial of ",n,"is",m)

#square of num
def square(n):
    return n*n
m=square(n)
print("square of ",n,"is",m)
 
####recursive functions
#factorial of a num
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
print("factorial of",n,"is",fact(n))

#finding power of given num
def power(r,n):
    if(n==0):
        return 1
    else:
        return r*power(r,n-1)
n=int(input("enter the base:"))
m=int(input("enter the power:"))
print(power(n,m))

#program to check two numbers are coprime or not
def gcd(m,n):
    if(m>n):
        a=m%n
        if(a==0):
            return n
        else:
            return gcd(n,a)
    else:
        a=m%n
        if(a==0):
            return m
        else:
            return gcd(m,a)
b=int(input("enter 1st number:"))
c=int(input("enter 2nd number:"))
d=gcd(b,c)
if(d==1):
    print(b,c,"both are coprimes")
else:
    print(b,c,"both are not coprimes")

#finding lcm of given number
def gcd(m,n):
    if(m>n):
        a=m%n
        if(a==0):
            return n
        else:
            return gcd(n,a)
    else:
        a=n%m
        if(a==0):
            return m
        else:
            return gcd(m,a)
b=int(input("enter 1st number:"))
c=int(input("enter 2nd number:"))
lcm=(b*c)/gcd(b,c)
print("LCM of",b,c,"is",lcm)

###Fibnocci series
##print nth number of the fibnocci series
def fibn(n):
    if(n<=1):
        return n
    else:
        return fibn(n-1)+fibn(n-2)
n=int(input("enter the nth number:"))
for i in range(n):
    fibn(i)
print(fibn(i))

#first n numbers of the fibnocci series
def fibn(n):
    if(n<=1):
        return n
    else:
        return fibn(n-1)+fibn(n-2)
n=int(input("enter the nth number:"))
for i in range(n):
    print(fibn(i))

##fibnocci series upto n numbers
def fibn(n):
    if(n<=1):
        return n
    else:
        return fibn(n-1)+fibn(n-2)
n=int(input("enter the number:"))
for i in range(n):
    if(fibn(i)<=n):
        print(fibn(i))
    else:
        break









