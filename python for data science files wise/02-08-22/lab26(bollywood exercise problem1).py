# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:03:14 2022

@author: DEEPTHI
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""1. How many records are present in the dataset? Print the metadata information of the dataset."""
data=pd.read_excel('bollywood.xlsx',index_col=0)
print(data)
data.info()
data.describe()
data.isnull().sum()


"""2. How many movies got released in each genre? Which genre had highest number of releases? Sort 
number of releases in each genre in descending order"""
maxu=data['Genre'].value_counts()
maxu[0:1]
maxu.index[0]

"""3. How many movies in each genre got released in different release times like long weekend, festive 
#season, etc. (Note: Do a cross tabulation between Genre and ReleaseTime.)"""
pd.crosstab(index=data['ReleaseTime'],columns=data['Genre'])


"""4. Which month of the year, maximum number movie releases are seen? (Note: Extract a new column 
called month from ReleaseDate column.)"""
data.insert(9,'month',0)
data['month']=pd.to_datetime(data['Release Date']).dt.month
maxi=data['month'].value_counts()
maxi[0:1]
maxi.index[0]

"""5. Which month of the year typically sees most releases of high budgeted movies, that is, movies with 
#budget of 25 crore or more?"""
pd.crosstab(index=data['month'],columns=data['BoxOfficeCollection'])

highbudge=data.loc[((data['Budget']>=25))]
budgetmax=highbudge['month'].value_counts()
budgetmax[0:1]

"""6"""
data.insert(10,'ROI',0)
data['ROI']=(data['BoxOfficeCollection']-data['Budget'])/data['Budget']
roi=data.sort_values('ROI',ascending=False)
roi['MovieName'][0:10]

"""7 Do the movies have higher ROI if they get released on festive seasons or long weekend? Calculate 
the average ROI for different release times."""
m=data.loc[(data['ReleaseTime']=='LW')]
m['ROI'].mean()
n=data.loc[(data['ReleaseTime']=='N')]
n['ROI'].mean()
o=data.loc[(data['ReleaseTime']=='FS')]
o['ROI'].mean()
p=data.loc[(data['ReleaseTime']=='HS')]
p['ROI'].mean()

if(m['ROI'].mean()>(n['ROI'].mean() and p['ROI'].mean()) or o['ROI'].mean()>(n['ROI'].mean() and p['ROI'].mean())):
    print("Movies have higher ROI if they get released on festive seasons or long weekends")


"""8 Draw a histogram and a distribution plot to find out the distribution of movie budgets. Interpret the 
#plot to conclude if the most movies are high or low budgeted movies"""

plt.hist(data["Budget"])
sns.distplot(data['Budget'])
print("from the histogram we can conclude that most of the movies are low budgeted movies")

"""Compare the distribution of ROIs between movies with comedy genre and drama. Which genre 
typically sees higher ROIs?"""
sns.distplot(data[data["Genre"]=="Comedy"]["ROI"])
sns.distplot(data[data["Genre"]==" Drama "]["ROI"])

"""Is there a correlation between box office collection and YouTube likes? Is the correlation positive or 
negative?"""
plt.scatter(data['BoxOfficeCollection'],data['YoutubeLikes'])
data["BoxOfficeCollection"].corr(data["YoutubeLikes"])
print("There is positive correlation")

"""Which genre of movies typically sees more YouTube likes? Draw boxplots for each genre of movies 
to compar"""

sns.boxplot(data=data, x='Genre', y='YoutubeLikes')
print("Action genre of movies typically sees more Youtube likes")


sns.pairplot(data)









