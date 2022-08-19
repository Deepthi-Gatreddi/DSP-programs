# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:41:34 2022

@author: DEEPTHI
"""

import matplotlib.pyplot as plt
num=[0.2,4,3,5,6,7,8,5]
plt.hist(num,bins=3)
plt.xlabel("numbers")
plt.ylabel("frequency")
plt.title("histogram")
plt.show()

import matplotlib.pyplot as plt
num=[0.2,4,3,5,6,7,8,5]
plt.hist(num,bins=3,color="hotpink")
plt.xlabel("numbers")
plt.ylabel("frequency")
plt.title("histogram")
plt.show()

import matplotlib.pyplot as plt
num=[0.2,4,3,5,6,7,8,5]
plt.hist(num)
plt.xlabel("numbers")
plt.ylabel("frequency")
plt.title("histogram")
plt.show()

