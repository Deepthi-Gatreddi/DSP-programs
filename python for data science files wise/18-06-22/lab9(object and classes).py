# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:11:36 2022

@author: DEEPTHI.
Object and classes
"""
class Person:
    "this is a person class"
    age=10
    def greet(self):
        print("hello")
    def soft(self):
        print("hello hai bye bye deepthi")
print(Person.age)
print(Person.greet)
print(Person.__doc__)

class Dog:
    animal='dog'
    def __init__(self,breed):
        self.breed=breed
    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color
Rodger=Dog("pug")
Rodger.setColor('brown')
print(Rodger.getColor())

class Person:
    attr1='deepthi'
    attr2='pavani'
    def fun(self):
        print("I'm a ",self.attr1)
        print("I'm a",self.attr2)
hoo=Person()
print(hoo.attr1)
hoo.fun()