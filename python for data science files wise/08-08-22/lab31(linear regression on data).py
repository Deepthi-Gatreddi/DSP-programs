# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:17:58 2022

@author: DEEPTHI
"""

#linear regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data=pd.read_csv("train.csv")
x=data['loan_amount']
x=np.array(x).reshape((-1,1))
y=data['loan_default']
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=0)
model=LinearRegression()
model.fit(x,y)
model.coef_
model.intercept_
pred=model.predict(test_x)
print(pred)
