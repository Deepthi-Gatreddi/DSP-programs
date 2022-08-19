# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:19:44 2022

@author: DEEPTHI
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.Series([1,3,20,4,6])
data.describe()
data.var()
y=pd.Series([data.mean(),data.median(),data.var(),data.std()])
plt.title("first sample")
plt.pie(y,labels=['mean','median','variance','standard deviation'],autopct='%1.1f%%')
plt.show()
sns.boxplot(y=data)


dataa=pd.Series([1,3,2,4,60])
dataa.describe()
dataa.var()
x=[dataa.mean(),dataa.median(),dataa.var(),dataa.std()]
plt.title("second sample")
plt.pie(x,labels=['mean','median','variance','standard deviation'],autopct='%1.1f%%')
plt.show()
sns.boxplot(y=dataa)


dat=pd.Series([1,10,70,60,20,100,5000])
dat.describe()
dat.var()
z=[dat.mean(),dat.median(),dat.var(),dat.std()]
print(z)
plt.title("Third sample")
plt.pie(z,labels=['mean','median','variance','standard deviation'],autopct='%1.1f%%')
plt.show()
sns.boxplot(y=dat)

datu=pd.Series([1,5,10,20,30,35])
datu.describe()
datu.var()
m=[datu.mean(),datu.median(),datu.var(),datu.std()]
print(m)
plt.title("Third sample")
plt.pie(m,labels=['mean','median','variance','standard deviation'],autopct='%1.1f%%')
plt.show()
sns.boxplot(y=datu)


dats=pd.Series([1,6,3,4,2,4,3,5,6,7,3,2,5,6,5,3,2,5,3,2,2,2])
dats.describe()
dats.mode()
dats.var()
n=[dats.mean(),dats.median(),dats.var(),dats.std()]
print(n)
plt.title("fourth sample")
plt.pie(n,labels=['mean','median','variance','standard deviation'],autopct='%1.1f%%')
plt.show()
sns.boxplot(y=dats)


date=pd.Series([2,5,6,4,3,5,6,6,6,5,3,2,2,4,5,4,3,5,6,7,8,8,9,8,64,3,3,2,43,55,67,3,56,96,4,3])
date.describe()
date.mode()
date.var()
r=[date.mean(),date.median(),date.var(),date.std()]
print(r)
plt.title("fifth sample")
plt.pie(r,labels=['mean','median','variance','standard deviation'],autopct='%1.1f%%')
plt.show()
sns.boxplot(y=date)

allu=[data.mean(),dataa.mean(),dat.mean(),datu.mean(),dats.mean(),date.mean()]

