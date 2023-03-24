"""
# File       : bs4Using.py
# Time       : 5:59 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
import re

from bs4 import BeautifulSoup

with open('test1.html', 'r+', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)
# get nodes attrs
# print(soup.title.name)  # get node's name
# print(soup.p.attrs)  # get node's attributes
# print(soup.p.attrs['name']) # get node's attribute's value
# print(soup.p['name'])
# print(soup.p['class'])
# get contents
# print(soup.p.string)
# print(soup.head.title)
# print(type(soup.head.title.string))
# print(soup.head.title.string)
# print(soup.div.contents)
# print(soup.div.children)
# for i, child in enumerate(soup.div.children):  # children only foreach every child
#     print(i, child)
# print(soup.div.descendants)  # generator could foreach every grandson's nodes
# for i, child in enumerate(soup.div.descendants):
#     print(i, child)
# print(soup.a.parent.prettify())
# print(list(enumerate(soup.a.parents)))
# # get brother nodes
# print('Next Sibling', soup.a.next_sibling)
# print("Prev Sibling", soup.a.previous_sibling)
# print("Next Siblings", list(enumerate(soup.a.next_siblings)))
# print("Prev Siblings", list(enumerate(soup.a.previous_siblings)))
# print('Next Sibling:')
# print(type(soup.a.next_sibling))
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.string)
# print('Parent:')
# print(type(soup.a.parents))
# print(soup.a.parents)
# print(list(soup.a.parents)[0])
# print(list(soup.a.parents)[0].attrs['class'])
# using find or findall
# using name get things
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)
# using attrs get things
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))
# using text get things text is a re expression object
# print(soup.find_all(text=re.compile('ar')))
# using find method get things
print(soup.find(name='ul'))  # only return first item
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))
