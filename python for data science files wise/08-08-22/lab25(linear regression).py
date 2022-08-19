# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:19:44 2022

@author: DEEPTHI
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
x=np.array([5,15,25,35,45,55]).reshape(-1,1)
y=np.array([5,20,14,32,22,38])
model=LinearRegression().fit(x,y)
r_sq=model.score(x,y)
print(r_sq)
print(model.intercept_)
print(model.coef_)
y_pred=(model.predict(x))
print(y_pred)
plt.scatter(x,y)
plt.plot(x,y_pred)
print(model.score(x,y_pred))
x_new=np.arange(5).reshape((-1,1))
print(x_new)
y_new=model.predict(x_new)
print(y_new)
print(model.score(x_new,y_new))
