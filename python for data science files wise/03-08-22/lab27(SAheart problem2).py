# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:21:45 2022

@author: DEEPTHI
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("SAheart.csv")

"""13. How many records are present in the dataset? Print the metadata information of the dataset."""
np.size(data)
print(data)
data.info()
data.isnull().sum()

"""14. Draw a bar plot to show the number of persons having CHD or not in comparison to they having 
family history of the disease or not."""
comp=pd.crosstab(data['chd'],data['famhist'])
r=np.arange(2)
plt.bar(r,comp['Absent'],color='r',width=0.25,label='Not having disease')
plt.bar(r+0.25,comp['Present'],color='g',width=0.25,label="having disease")
plt.xticks(r+(0.25/2),[0,1])
plt.legend()

"""Does age have any correlation with sbp? Choose appropriate plot to show the relationship"""
plt.scatter(data['age'],data['sbp'])
data['age'].corr(data['sbp'])
print("it has a positive correlation")

"""Compare the distribution of tobacco consumption for persons having CHD and not having CHD. 
Can you interpret the effect of tobacco consumption on having coronary heart disease?"""
sns.boxplot(data['chd'],data['tobacco'])


"""How are the parameters sbp, obesity, age and ldl correlated? Choose the right plot to show the 
relationships"""

coril=data.corr()

"""Derive a new column called agegroup from age column where persons falling in different age ranges 
are categorized as below.
(0–15): young
(15–35): adults
(35–55): mid
(55–): old"""
data.insert(6,'agegroup',0)
for i in range(len(data['age'])):
    if(data['age'][i]>0 and data['age'][i]<=15):
        data['agegroup'][i]='young'
    elif(data['age'][i]>15 and data['age'][i]<=35):
        data['agegroup'][i]='adults'
    elif(data['age'][i]>35 and data['age'][i]<=55):
        data['agegroup'][i]='mid'
    else:
        data['agegroup'][i]='old'


"""Find out the number of CHD cases in different age categories. Do a barplot and sort them in the 
order of age groups."""
romp=pd.crosstab(data['chd'],data['agegroup'])
r=np.arange(2)
plt.bar(r,romp['adults'],color='r',width=0.2,label='adults')
plt.bar(r+0.2,romp['mid'],color='g',width=0.2,label="mid")
plt.bar(r+0.4,romp['old'],color='b',width=0.2,label='old')
plt.bar(r+0.6,romp['young'],color='orange',width=0.2,label="young")
plt.xticks(r+(0.75/2),[0,1])
plt.legend()

"""Draw a box plot to compare distributions of ldl for different age groups."""

sns.boxplot(data['agegroup'],data['ldl'])

