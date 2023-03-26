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
# get information
# get attrs and attrs' values
# a = doc('.list#list-1')
# print(a, type(a))
# print(a.attr('data-name'))
# print(a.attr.data)
# foreach get items attr's values
# a = doc('li')
# for item in a.items():
#     print(item.attr('class'))
# get text content
# a = doc('.list#list-1 .element#selected span')
# print(a)
# print(a.text())
# print(a.html())
# li = doc('li')
# print(li.html())
# print(li.text())
# print(type(li.text()))
# nodes action
# li = doc('.list#list-1')
# print(li)
# li.remove_class('list')
# print(li)
# li.add_class('list4')
# print(li)
# li.remove_attr('data-name')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('Changed')
# print(li)
# li.html('<span>changed item</span>')
# print(li)
# doc = pq(filename='test1.html')
# li = doc('.list#list-1')
# li.find('#need').remove()
# print(li)
# faked class selector
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(Foo)')
print(li)

