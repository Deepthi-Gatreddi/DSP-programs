# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:05:50 2022

@author: DEEPTHI
"""
import pandas as pd
import numpy as nd
data=pd.read_csv("Data.csv")
print(data)
data.columns
pd.read_csv("Data.csv",header=None)
pd.read_csv("Data.csv",header=None,skiprows=1)
data.dtypes
data['age']=data['age'].astype(float)
data.dtypes
data.isna().sum()
data.insert(11,"age_convert",0)
print(data)
data.dtypes
data.info()
data["age_convert"]
data[2:]
data[2:3]
data[2:5]
data['marital'].unique()
data.describe()
data['age'].describe()
data['age_convert']=data['age'].mean()
data['age_convert']
data['age_convert']=data['age'].median()
data['age_convert']
data.isnull().sum()

