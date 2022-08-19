# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 08:51:43 2022

@author: DEEPTHI
"""

import pandas as pd
datafraame=pd.Series([23,43,54])   #creating dataframe using series
print(datafraame)
a=pd.Series([23,45,54],index=[5,3,6])    
print(a)
aa=pd.DataFrame({"pav":[23],"deep":[54]}) #creating dataframe using dataframe
print(aa)
dict={"one":1,"Two":2,"three":3}
df=pd.Series(dict)
print(df)
data=pd.read_csv("DATA.csv")
print(data)
data.info()
data.head()
data.tail()
data.head(7)
data.tail(10)
print(type(data))
data.describe()
data["age"]<=30
data.loc[5]
data.loc[data["age"]>80]
data.loc[1]
data.loc[1,"id"]
#ewdata=data[(data.age>60)&(data.month>5)]
data.to_excel("record1.xlsx",sheet_name="sl")
data=pd.read_excel("record1.xlsx")
print(data)
data.job[1:4],data.poutcome[5:6]  
data.iloc[2:5,3:7]
data.iloc[2:4,[2,6,3]]
data.iloc[[6,4,7],[2,5]]




