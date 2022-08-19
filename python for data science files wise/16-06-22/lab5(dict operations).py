# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:53:29 2022

@author: DEEPTHI
dictionary operations
"""
dic={1:"deepthi",2:"kam",3:"bam"}
print(type(dic))
di=dic.copy()
print(di)
dic.fromkeys([2,"bam"])
dic.items()
dic.keys()
dic.pop(2)
print(dic)
dic.popitem()
print(dic)
dic.update({2:"kam"},{3:"bam"})
dic.update({2:"kam"})
print(dic)
dic.values()
di.clear()
print(di)
dic.get(2) #it returns the vlaue of the item with the specified key
dic.get(2,"kam")
dic.setdefault(2) 
dic.setdefault(3) #returns the value of the item with the specified key if the key does not exist insert the key with the specified value
dic.setdefault(4,"pam")
print(dic)

