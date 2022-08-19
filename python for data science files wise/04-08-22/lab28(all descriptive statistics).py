# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 11:48:09 2022

@author: DEEPTHI
"""

import pandas as pd 
df=pd.read_csv("train.csv")
type(df)
list(df.columns) 
df.head(5)
df.head(5).transpose() 
df.shape
df.info()
df[0:5]
df[-5:]  
df['education'][0:5] 
df[['loan_id', 'loan_amount']][0:5] 
df.iloc[4:9, 1:4] 
df.education.value_counts() 
df.age.value_counts(normalize=True)
pd.crosstab( df['education'],df['no_of_loans'] ) 
df[['loan_id', 'age']].sort_values('age', ascending = False)[0:5] 
df["no_of_paid_loans"]=df["no_of_loans"]-df["no_of_curr_loans"]
df[['loan_id','age','education']][0:5]
df[['loan_id','age','education','loan_amount']].sort_values('loan_amount',ascending=False)[0:5]
df.groupby('age')['loan_amount'].mean()
df.groupby('age')['loan_amount'].mean().sort_index()
df.rename(columns={'loan_default':'loan_def','education':'edu'},inplace=True)
df[df['age']>=50][['proof_submitted','edu']]
df.drop( 'proof_submitted', inplace = True, axis = 1)
df.isnull().sum()
df=df.dropna(subset=['edu'])
