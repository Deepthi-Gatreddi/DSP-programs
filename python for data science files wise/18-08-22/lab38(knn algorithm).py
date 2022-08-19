# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:14:53 2022

@author: DEEPTHI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data=pd.read_csv("HR_comma_sep.csv")
print(data)
x=data.drop(columns=['Department','left'],axis=1)
y=data['left']
x=pd.get_dummies(x)
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.3,random_state=0)
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(train_x,train_y)
pred=knn.predict(test_x)
accuracy_score(test_y,pred)


