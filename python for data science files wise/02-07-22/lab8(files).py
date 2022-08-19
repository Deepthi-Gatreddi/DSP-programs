# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:06:23 2022

@author: DEEPTHI
files
"""
file=open("new.txt",'w')
file.write("hey hai welcome my programming world")
file.close()

file=open("new.txt",'r')
file.read(5)
file.read()
file.close()

file=open("new.txt",'a')
file.write("this is another line")
file.write("\n adding new line")
file.append("what is this")
file.close()

file=open("new.txt",'r')
file.read()
file.readline()
file.readlines()
file.close()

file=open("new.txt",'r')
file.read()
file.tell()
file.seek(5)
file.readline()
file.readlines()
file.close()

file=open("new.txt",'x')
file.close()

file=open("abc.txt","w")
file.write("hey dee")
file.close()

file=open("abc.txt",'r+')
file.append("this is line")
file.close()

file=open("new2.txt",'w')
lines=['this is line 1','\nthis is line 2']
file.writelines(lines)
file.close()

file=open('new2.txt','r')
file.read()
file.close()

file=open("new2.txt",'r')
file.readlines()
file.close()

file=open('new2.txt','r')
for line in file:
    print(line,end='')
file.close()

file=open("new3.txt",'w')
lines=['this is first line','\n This is second line2','\n This is third line3','\n This is fourth line4']
file.writelines(lines)
file.close()

file=open("new3.txt",'r')
file.readlines()
file.close()

#print a particular line from a file
m=int(input("enter a number:"))
file=open("new3.txt",'r')
currentline=1
for line in file:
    if currentline == m:
        print(line)
        break
    currentline=currentline+1
file.close()

#finding no of characters words and newlines in a file
file=open("new3.txt",'r')
char=0
words=0
line=0
for i in file:
    line=line+1
    for r in i:
        char=char+1
        if(r==' '):
            words=words+1
print("Number of words in the file is",words)
print("Number of characters in the file is",char)
print("Number of lines in the given file is",line)