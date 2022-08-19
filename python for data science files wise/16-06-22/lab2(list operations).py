# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 13:15:21 2022

@author: DEEPTHI
List operations
"""
lis=[8,"deepthi",1]
lis1=[3,1,4]
print(type(lis))
print(type(lis1))
lis1.append(1)
print(lis1)
lis1.extend([2,3])
print(lis1)
lis.insert(2,4)
print(lis)
lis.remove(1)
print(lis)
lis1.pop(1)
print(lis1)
lis[0:1]
lis[1:]
lis[-3:]
lis[-3:-1]
lis.reverse()
print(lis)
len(lis)
min(lis)
max(lis)
min(lis1)
max(lis1)
lis.count(4)
lis+lis1
lis*2
lis.index('deepthi')
lis.sort()
lis1.sort()
print(lis1)
lis.clear()
print(lis)


