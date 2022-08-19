# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:54:14 2022

@author: DEEPTHI
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3])
y=np.array([3,8,6,10])
plt.subplot(1,2,1) # row,column,number of the plot
plt.plot(x,y)

x=np.array([0,1,2,3])
y=np.array([23,4,3,45])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()



x=np.array([0,1,2,3])
y=np.array([3,8,6,10])
plt.subplot(1,2,1)
plt.plot(x,y)

x=np.array([0,1,2,3])
y=np.array([23,4,3,45])
plt.subplot(1,2,2)
plt.pie(y)
plt.show()



x=np.array([0,1,2,3])
y=np.array([3,8,6,10])
plt.subplot(1,2,1)
plt.bar(x,y,color='y')

x=np.array([0,1,2,3])
y=np.array([23,4,3,45])
plt.subplot(1,2,2)
plt.pie(y)
plt.show()


x=np.array([0,1,1,1])
y=np.array([23,4,3,45])
plt.subplot(2,2,1)
plt.pie(y)
plt.show()

x=np.array([0,1,2,3])
y=np.array([3,8,6,10])
plt.subplot(2,2,2)
plt.bar(x,y,color='y')

x=np.array([0,1,2,3])
y=np.array([23,30,10,45])
plt.subplot(2,2,3)
plt.pie(y)
plt.show()

x=np.array([0,1,2,3])
y=np.array([3,8,6,10])
plt.subplot(2,2,4)
plt.bar(x,y,color='r')



