# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 09:58:27 2022

@author: DEEPTHI
STRING OPERATIONS
"""

str="my name is DEEPTHI {} {}"
print(type(str))
#capitalize
str.capitalize() #converts first character to capital
str.casefold()   #converts all character to lower case
str.upper()      #converts all characters to upper case
str.lower()      #converts all characters to lower case
str.count("e")   #gives the count of given element 
str.endswith("HI") #return true if str ends with HI
str.endswith("}")
str.startswith("mo") #return true if str startswith mo
str.find("is")       #finds the index of the first element given
str.find("i")
#format
str.format(18,39)  #formats the string
str.format(1,2)
str.index("D")    #returns the index postion of the given element
str.index("is")
str.isalnum()    #return true is all the charcters alphabets or numbers
str.isupper()   # if all are upper case
str.islower()
str.isdigit()
str.isalpha()
str.replace("DEEPTHI","kavya")  #replaces old string with new string
str.split("i")   #splits based on given parameter
str.split(" ")
str.swapcase() #converts uppercase to lower case and vice versa
str.title()   #converts first letter of everyword to captial
str[1:2]     #accesing the elements
str[1:]
str[:4]
str[:-4]
str[-9:-2]
str[-2:]
str[-7]
str[-7:]


