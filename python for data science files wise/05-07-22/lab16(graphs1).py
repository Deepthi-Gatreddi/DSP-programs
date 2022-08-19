# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:24:16 2022

@author: DEEPTHI
"""
import matplotlib.pyplot as plt
import numpy as np
plt.title("line plot")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
xpoints=np.array([1,10])
ypoints=np.array([1,30])
plt.plot(xpoints,ypoints)
plt.show()

plt.plot([3,2],[16,20],'--')
plt.show()

x=[2,6,3,4]
y=[5,6,8,10]
plt.scatter(x,y)
plt.show()

xpoints=np.array([2,4,6,7])
ypoints=np.array([12,34,45,65])
plt.plot(xpoints,ypoints)
plt.show()

ypoints=np.array([12,34,45,65])
plt.plot(ypoints,marker='*',mec='b',color='r')
plt.show()

ypoints=np.array([12,34,45,65])
plt.plot(ypoints,marker='*',mec='b',color='r',linewidth='12')
plt.show()

xpoints=np.array([1,5,5,1,1,3,1,5,5,3,1])
ypoints=np.array([1,1,5,5,1,3,1,5,1,3,5])
plt.plot(xpoints,ypoints,marker='*',mec='r')
plt.show()

xpoints=np.array([1,1,5,5,1,5,11,5,11])
ypoints=np.array([1,5,5,1,1,1,3,5,3])
x=(1.5,1.5,2,2,2.5,2.5,3,3,3.5,3.5,4,4,4.5,4.5)
y=(1,5,5,1,1,5,5,1,1,5,5,1,1,5)
xx=(2,4)
yy=(8,8)
plt.plot(ypoints,xpoints,marker='*',mec='r')
plt.plot(x,y,marker='*',mec='r')
plt.plot(xx,yy,marker='*',mec='r')
plt.show()
