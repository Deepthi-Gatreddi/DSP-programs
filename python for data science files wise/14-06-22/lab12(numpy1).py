# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:45:05 2022
code on numpy operations on 10/06/2022

@author: DEEPTHI
"""

import numpy as np
arrex=np.arange(6)
arrex1=np.array([[6,3,2,8],[2,5,1,4]],dtype=int)
arrex2=np.array([10,2,4,18],dtype=int)
arrex3=np.array([2,9,7,8],dtype=int)
print(arrex)
print(arrex1)
np.shape(arrex)
np.shape(arrex1)
np.size(arrex)
np.size(arrex1)
np.linspace(2,5,5)
np.ones(2)
np.zeros((2,2))
np.sort(arrex1)
np.concatenate((arrex,arrex2))
np.concatenate((arrex2,arrex3))
np.concatenate((arrex2,arrex3),axis=0)
arrex.ndim
arrex1.ndim
arrex.shape
arrex1.shape
arrex2.size
arrex1.size
arrex.reshape(3,2)
b=arrex.copy()
print(b)
arrex.sum()
arrex*arrex
arrex1+arrex1
arrex3-arrex2
arrex2.min()
arrex.min()
arrex3.max()
arrex2.max()
np.unique(arrex1)
arrex1.transpose()
np.flip(arrex1)
arrex[2:5]
np.add(arrex2,arrex3)
np.subtract(arrex2,arrex3)

