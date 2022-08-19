# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:12:26 2022

@author: DEEPTHI
"""
"""ort requests as rq
page=rq.get("http://www.google.com?")
print(page)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
page_title=soup.title.text
print(page_title)
page_body=soup.body
print(page_body)
page_head=soup.head
print(page_head)"""
import urllib.request
url="https://www.google.com?"
resp=urllib.request.urlopen(url)
page1=resp.read()
page=str.read()
page=str(page1)
def getURL(page):
    start_link=page.find("<a href")
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=page[start_quote+1:end_quote]
    return url,end_quote
while True:
    url,n=getURL(page)
    page=page[n:]
    if url:
        print(url)
    else:
        break

    