"""
# File       : xpathUsing.py
# Time       : 5:27 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
from lxml import etree
# text = '''
# <div>
#     <ul>
#         <li class="item-0"><a href="link1.html">first item</a></li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-active"><a href="link3.html">third item</a></li>
#         <li class="item-1"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))
html = etree.parse('test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))
# result = html.xpath('//*')
# print(result)
# rs1 = html.xpath('//li/a')
# print(rs1)
# rs2 = html.xpath('//ul//a')
# print(rs2)
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)
# result = html.xpath('//li[@class="item-0"]')
# print(result)
# result = html.xpath('//li[@class="item-0"]//text()')
# result1 = html.xpath('//li[@class="item-0"]/a/text()')
# print(result, result1)
# result = html.xpath('//li/a/@href')  # get nodes properties values
# print(result)
# text = '''
# <li class='li li-first' name="hello"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)
# result = etree.HTML('//li[contains(@class, "li") and @name="hello"]/a/text()')
# print(result)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)