# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:16:20 2022

@author: DEEPTHI
"""

import pandas as pd
import numpy as np
dataa=pd.read_csv("cars_sampled.csv")
data=dataa.copy()
print(data)
data.isnull().sum()
data.dtypes
data.info()
data.dropna(inplace=True)
data.dropna(axis=0,inplace=True)
data.isnull().sum()
data.insert(11,'powerPSu',0)
def change(val,maxu):
    valu=val/maxu
    return valu
data['powerPSu']=change(data['powerPS'],data['powerPS'].max())
data['powerPSu']=round(data['powerPSu'],4)
data.insert(11,'powerPSu1',0)
def changed(val,maxu,minu):
    valu=(val-minu)/(maxu-minu)
    return valu
data['powerPSu1']=changed(data['powerPS'],data['powerPS'].max(),data['powerPS'].min())
data['powerPSu1']=round(data['powerPSu1'],3)
data.insert(11,'powerpsu2',0)
def changes(val,meen,stdu):
    valu=(val-meen)/stdu
    return valu
data['powerpsu2']=changes(data['powerPS'],data['powerPS'].mean(),data['powerPS'].std())
data['powerpsu2']=round(data['powerpsu2'],2)
#data formatting
data['name']=data['name'].str.lower()
data['fuelType']=data['fuelType'].str.replace("l","")
data["powerPS"].replace(150,"one fifty ",inplace=True)
#to remove space at the ends
data['name']=data['name'].str.lstrip()
#data binning
minval=data['price'].min()
print(minval)
maxval=data['price'].max()
print(maxval)
bins=np.linspace(minval,maxval,4)
print(bins)
labels=['low','medium','high']
data['bins']=pd.cut(data['price'],bins=bins,labels=labels,include_lowest=True)
print(data['bins'].describe())




