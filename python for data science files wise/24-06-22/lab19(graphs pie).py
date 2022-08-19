# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:47:04 2022

@author: DEEPTHI
"""

import matplotlib.pyplot as plt
import numpy as np
y=np.array([20,34,54,25])
plt.pie(y)
plt.show()

y=np.array([20,34,25])
co=['r','b','green']
plt.pie(y,colors=co,labels=['dsp','wt','or'])
plt.legend()
plt.show()

y=np.array([20,34,25])
co=['r','b','green']
plt.pie(y,colors=co,labels=['dsp','wt','or'])
plt.legend(title='exams data')
plt.show()

