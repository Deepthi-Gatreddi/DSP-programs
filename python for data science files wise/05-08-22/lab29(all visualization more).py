# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:18:51 2022

@author: DEEPTHI
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv("train.csv")
sns.barplot(df['education'],df['loan_default'])
sns.barplot(df['education'],df['loan_default'],df['last_delinq_none'])
plt.hist(df['loan_amount']) 
plt.hist(df['loan_amount'],bins=5)  
sns.distplot(df['loan_amount'])
sns.boxplot(df['asset_cost'])
sns.distplot(df['asset_cost'])
box=plt.boxplot(df['asset_cost'])
[item.get_ydata()[0] for item in box['caps']]
[item.get_ydata()[0] for item in box['whiskers']] 
[item.get_ydata()[0] for item in box['medians']]
sns.distplot(df[df['last_delinq_none'] == 1]['loan_default'], color = 'y', label = 'last_delinq_none=1') 
sns.distplot(df[df['last_delinq_none'] == 0]['loan_default'], color = 'r', label = 'last_delinq_none=0'); 
plt.legend() 
sns.boxplot(df['proof_submitted'],df['loan_default']);

sns.regplot(x='age',y='loan_amount',data=df)
sns.pairplot(df)


