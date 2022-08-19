# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:18:21 2022

@author: DEEPTHI
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("company_sales_data.csv")
print(data)
profitList= data['total_profit'].tolist()
monthList= data['month'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
#plt.xticks(monthList)
plt.title('Company profit per month')
#plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()



plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
      
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()


monthList  =data['month'].tolist()
faceCremSalesData   = data['facecream'].tolist()
faceWashSalesData   = data['facewash'].tolist()
toothPasteSalesData = data['toothpaste'].tolist()
bathingsoapSalesData   = data['bathingsoap'].tolist()
shampooSalesData   = data['shampoo'].tolist()
moisturizerSalesData = data['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()


monthList  =data['month'].tolist()
toothPasteSalesData = data['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Tooth paste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()


monthList  = data['month'].tolist()
faceCremSalesData   = data['facecream'].tolist()
faceWashSalesData   = data['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()


monthList  = data['month'].tolist()
bathingsoapSalesData   = data['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title(' Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('bathingsoap sales data')
#plt.savefig('D:\Python\Articles\matplotlib\sales_data_of_bathingsoap.png', dpi=150)
plt.show()



profitList =data['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()


monthList  = data['month'].tolist()

labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData   = [data['facecream'].sum(), data['facewash'].sum(),data['toothpaste'].sum(), 
         data['bathingsoap'].sum(), data['shampoo'].sum(),data['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()



monthList  =data['month'].tolist()
bathingsoap   = data['bathingsoap'].tolist()
faceWashSalesData   =data['facewash'].tolist()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthList, bathingsoap, label = 'Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of  a Bathingsoap')
axarr[1].plot(monthList, faceWashSalesData, label = 'Face Wash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales data of  a facewash')

plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.show()


monthList  =data['month'].tolist()

faceCremSalesData   = data['facecream'].tolist()
faceWashSalesData   = data['facewash'].tolist()
toothPasteSalesData = data['toothpaste'].tolist()
bathingsoapSalesData   = data['bathingsoap'].tolist()
shampooSalesData   = data['shampoo'].tolist()
moisturizerSalesData = data['moisturizer'].tolist()

plt.plot([],[],color='m', label='face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)

plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData, 
              bathingsoapSalesData, shampooSalesData, moisturizerSalesData, 
              colors=['m','c','r','k','g','y'])

plt.xlabel('Month Number')
plt.ylabel('Sales unints in Number')
plt.title('Alll product sales data using stack plot')
plt.legend(loc='upper left')
plt.show()

data.info()
x=data['month']
y=data['facecream']
plt.pie(y)
plt.show()

x=data['month']
y=data['total_profit']
plt.plot(x,y)
plt.show()

x=data['month']
y=data['facecream']
plt.bar(x,y)
plt.show()
plt.scatter(x,y)
plt.show()

print(profitList)
print(y)
