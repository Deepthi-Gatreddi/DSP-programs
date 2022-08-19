# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:35:11 2022

@author: DEEPTHI
"""

import matplotlib.pyplot as plt
country=["india","usa","germany","france","africa"]
gdp=[25355,46636,34646,97377,43333]
plt.bar(country,gdp)
plt.title("country's gdp using bar plot")
plt.xlabel("country")
plt.ylabel("gdp")
plt.show()

import matplotlib.pyplot as plt
country=["india","usa","germany","france","africa"]
gdp=[25355,46636,34646,97377,43333]
plt.barh(country,gdp)
plt.title("country's gdp using bar plot")
plt.xlabel("country")
plt.ylabel("gdp")
plt.show()

import matplotlib.pyplot as plt
country=["india","usa","germany","france","africa"]
gdp=[25355,46636,34646,97377,43333]
plt.bar(country,gdp,color='r')
plt.title("country's gdp using bar plot")
plt.xlabel("country")
plt.ylabel("gdp")
plt.show()
