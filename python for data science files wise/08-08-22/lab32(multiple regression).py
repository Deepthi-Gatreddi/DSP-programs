# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:19:44 2022

@author: DEEPTHI
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
x=[[0,1],[5,1],[15,2],[25,5],[35,11],[45,15],[55,34],[60,35]]
print(x)
y=[4,5,20,14,32,22,38,43]
x,y=np.array(x),np.array(y)
model=LinearRegression().fit(x,y)
r_sq=model.score(x,y)
print(r_sq)
print(model.intercept_)
print(model.coef_)
y_pred=(model.predict(x))
print(y_pred)
print(model.score(x,y_pred))
x_new=np.arange(10).reshape((-1,2))
y_new=model.predict(x_new)
print(y_new)
