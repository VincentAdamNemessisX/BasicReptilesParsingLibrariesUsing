"""
# File       : pyqueryUsing.py
# Time       : 9:10 AM
# Author     : vincent
# version    : python 3.8
# Description:
"""
import requests
from pyquery import PyQuery as pq
# sample for simply using pyquery
# with open('test1.html', 'r+', encoding='utf-8') as f:
#     html = f.read()
doc = pq(filename='test1.html')
# print(doc('li'))
# doc = pq(url='http://www.vincentadamnemessis.site')
# print(doc('title'))
# doc = pq(requests.get('http://www.vincentadamnemessis.site').text)
# print(doc('title'))
# print(doc('.list .element'))
# print(type(doc('.list .element')))
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)
# lis = items.children()
# print(lis)
# container = items.parent()
# print(type(container))
# print(container)
# print(items.parents())
# print(items.siblings())
# li = doc('.list#list-1')
# print(li)
# print(str(li))
# for each element
# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li, type(li))


