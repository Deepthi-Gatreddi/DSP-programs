# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:16:28 2022

@author: DEEPTHI
set operations
"""
setu={1,2,"deepthi"}
setu1={4,3,1}
print(type(setu))
setu.add(4)
print(setu)
setu|setu1
setu&setu1
setu1-setu
se=setu.copy()
print(se)
setu1.update([2,3])
print(setu1)
setu.capitalize() #errpr
setu.clear()
print(setu)