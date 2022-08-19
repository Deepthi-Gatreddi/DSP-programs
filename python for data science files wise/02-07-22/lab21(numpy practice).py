# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 09:02:43 2022

@author: DEEPTHI
"""

#to know version of numpy
import numpy as np
import pandas as pd
print(np.__version__)
#help on add function
print(np.info(np.add))
#to know zeros
arr=np.array([1,3,4])
print(np.all(arr))
arrr=np.array([0,2,3,4])
print(np.all(arrr))
print(np.any(arrr))
ar=np.array([0,0,0,0])
print(np.any(ar))
#to know infinite values
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))
np.isnan(a)


a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))
 
#to check two arrays are same or not
a=np.array([1,2,3])
b=np.array([1,2,3])
count=0
for i in range (0,(len(a))):
  if(a[i]==b[i]):
    count=count+1
print(count)
if(count==(len(a))):
  print("both arrays are same")
else:
    print("they both are not same")
    
x = np.array([3, 5])
y = np.array([2, 5])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x, y))
print("Comparison - greater_equal")
print(np.greater_equal(x, y))
print("Comparison - less")
print(np.less(x, y))
print("Comparison - less_equal")
print(np.less_equal(x, y))

x = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("Original numbers:")
print(x)
print(y)
print("Comparison - equal:")
print(np.equal(x, y))
print("Comparison - equal within a tolerance:")
print(np.allclose(x, y))

X = np.array([1, 7, 13, 105])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))


array=np.zeros(10)
print("An array of 10 zeros:")
print(array)
array=np.ones(10)
print("An array of 10 ones:")
print(array)
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)


x = np.array([3, 5])
y = np.array([2, 5])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x, y))
print("Comparison - greater_equal")
print(np.greater_equal(x, y))
print("Comparison - less")
print(np.less(x, y))
print("Comparison - less_equal")
print(np.less_equal(x, y))


X = np.array([1, 7, 13, 105])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))

array=np.arange(30,71)
print("Array of the integers from 30 to70")
print(array)

array_2D=np.identity(3)
print('3x3 matrix:')
print(array_2D)

rand_num = np.random.normal(0,1,1)
print("Random number between 0 and 1:")
print(rand_num)


rand_num = np.random.normal(6,88,15)
print("15 random numbers from a standard normal distribution:")
print(rand_num)

v = np.arange(15,55)
print("Original vector:")
print(v)
print("All values except the first and last of the said vector:")
print(v[1:-1])

a = np.arange(10,22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
  print(x,end=" ")

v = np.linspace(10, 49, 5)
print("Length 10 with values evenly distributed between 5 and 50:")
print(v)

x = np.arange(21)
print("Original vector:")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1
print(x)

x = np.random.randint(0, 11, 5)
print("Vector of length 5 filled with arbitrary integers from 0 to 10:")
print(x)


m= np.arange(10,22).reshape((3, 4))
print(m)

m= np.arange(10,22).reshape((3, 4))
print("Original matrix:")
print(m)
print("Number of rows and columns of the said matrix:")
print(m.shape)

x = np.eye(3)
print(x)x = np.eye(3)
print(x)


