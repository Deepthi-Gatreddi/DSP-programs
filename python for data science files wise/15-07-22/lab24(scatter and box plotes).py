# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:11:49 2022

@author: DEEPTHI
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x=[2,3,5,6,7,7,8,9,10,11]
y=[99,98,97,87,65,55,55,22,12,11]
color=['red','blue','green','orange','red','blue','pink','yellow','orange','red']
size=np.random.rand(10)
plt.scatter(x,y,c=color,s=size*1000)
plt.show()

x=np.random.rand(40)
y=np.random.rand(40)
z=np.random.rand(40)
colors=np.random.rand(40)
plt.scatter(x,y,s=z*1000,c=colors,alpha=0.8)
plt.show()


data=[10,20,30,40,50,70]
plt.boxplot(data)
plt.show()
 
df=pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
df.plot.box()

df=pd.DataFrame(np.random.rand(10,5)*100,columns=['A','B','C','D','E'])
df.plot.box()
