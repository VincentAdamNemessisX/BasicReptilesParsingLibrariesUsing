# BasicReptilesParsingLibrariesUsing
# Parsing Libraries


## XPath
### 常用规则:
|表达式|描述|
| :-----: | :-----: |
|nodename|选取此节点的所有子节点|
|/|从当前节点选取直接子节点|
|//|从当前节点选取子孙节点|
|.|选取当前节点|
|..|选取当前节点的父节点|
|@|选取属性|



### etree read html string demo:
```python
from lxml import etree
text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-active"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
```
### etree read html file demo:
```python
html = etree.parse('test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
```
### using xpath get some sample nodes:
```python
html = etree.parse('test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))
result = html.xpath('//*')
print(result)
rs1 = html.xpath('//li/a')
print(rs1)
rs2 = html.xpath('//ul//a')
print(rs2)
```
### using xpath get nodes demo:
```python
result = html.xpath('//li[@class="item-0"]')
print(result)
```
### using xpath get text:
```python
result = html.xpath('//li[@class="item-0"]//text()')
result1 = html.xpath('//li[@class="item-0"]/a/text()')
print(result, result1)
out:
['\n        ', 'first item', '\n    ', '\n        ', 'fifth item', '\n    '] ['first item', 'fifth item']
```
### using xpath get nodes properties values:
```python
result = html.xpath('//li/a/@href')  # get nodes properties values
print(result)
out:
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
```
### using xpath get nodes properties that with multi-values:
```python
text = '''
<li class='li li-first'><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
out:
['first item']
```
### using xpath get nodes multi-properties:
```python
text = '''
<li class='li li-first' name="hello"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)
result = etree.HTML('//li[contains(@class, "li") and @name="hello"]/a/text()')
print(result)
out:
<Element html at 0x10752fb80>
```
### xpath 运算符：
|运算符|描述|实例|返回值|
| :-----: | :-----: | :-----: | :----- |
|or|或|age =19 or age = 20|如果 age是 19，贝lj返回 true。 如果 age是 21，则返回 false|
|and|与|age>19 and age<21|如果 age是 20，则返回 true。 如果 age是 18，则返回 false|
|mod|计算除法的余数|5 mod 2|1|
|||计算两个节点集|//book | //cd|返回所有拥有 book 和 cd 元素的节点集|
|+|加法|6 + 4|10|
|\-|减法|6 - 4|2|
|\*|乘法|6 \* 4|24|
|div|除法|8 div 4|2|
|\=|等于|age=19|如果 age 是19，则返回 true，如果 age是其他，则返回false|
|!=|不等于|age!=19|如果 age 是其他，则返回 true，如果 age 是19，则返回false|
|<|小与|age<19|如果 age 小与19，则返回 true，如果 age 大于或等于19，则返回false|
|<=|小于或等于|age<=19|如果 age小与或等于19，则返回true，如果 age 大于19，则返回 false|
|\>|大于|age>19|如果 age大于19，则返回 true，如果 age 小与或等于19，则返回 false|
|\>=|大于或等于|age>=19|如果 age 大于或等于19，则返回 true，如果 age小与19，则返回 false|





### 按序选择：
```python
#序号是以 1开头
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)
out:
['first item']
['fifth item']
['first item', '\n        second item']
['third item']
```
#### [按序选择深入](http://www.w3school.com.cn/xpath/xpath%20_functions.asp)
### 节点轴选择：
```python
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
out:
[<Element html at 0x10de24780>, <Element body at 0x10de248c0>, <Element ul at 0x10de24900>, <Element div at 0x10de24940>]
[<Element div at 0x10de24940>]
['item-0']
[<Element a at 0x10de24900>]
[<Element span at 0x10de24880>]
[<Element a at 0x10de24840>]
[<Element li at 0x10de247c0>, <Element li at 0x10de248c0>, <Element li at 0x10de24980>, <Element li at 0x10de24a00>]
```
第一次选择时，我们调用了 ancestor轴，可以获取所有祖先节点。 其后需要跟两个冒号，然后是 节点的选择器，这里我们直接使用\*，表示匹配所有节点，因此返回结果是第一个 li节点的所有祖先 节点，包括 html、 body、 div 和 ul。

第二次选择时，我们又加了限定条件，这次在冒号后面加了 div，这样得到的结果就只有 div 这 个祖先节点了 。

第三次选择时，我们调用了 attribute轴，可以获取所有属性值，其后跟的选择器还是\*，这代表 获取节点的所有属性，返回值就是 li节点的所有属性值。

第四次选择时，我们调用了 child 轴，可以获取所有直接子节点 。 这里我们又加了限定条件，选 取 href 属性为 linkl.html 的 a 节点 。

第五次选择时，我们调用了 descendant 轴，可以获取所有子孙节点 。 这里我们又加了限定条件获 取 span节点，所以返回的结果只包含 span节点而不包含 a节点。

第六次选择 时，我们调用 了 following 轴，可以 获取当前节点之后的所有节点 。 这里我们虽然使用的是\*匹配，但又加了索引选择，所以只获取了第二个后续节点 。

第七次选择时，我们调用 了 following-sibling 轴 ，可以获取当前节点之后的所有同级节点 。 这里我们使用\*匹配，所以获取了所有后续同级节点。

以上是 XPath轴的简单用法， 更多轴的用法可以参考: [xpath 节点轴选择详细](http://www.w3school.eom.cn/xpath/xpath_axes.aspx)

## BeautifulSoup4
|解析器|使用方法|优势|劣势|
| :-----: | :-----: | :----- | ----- |
|Python 标准库|BeautifulSoup(markup, "html.parser")|Python 的内置标准库、执行速度适中、文档容错能力强|Python 2.7.3及 Python 3.2.2 之前的版本文档容错能力差|
|lxml HTML解析器|BeautifulSoup(markup, "lxml")|速度快，文档容错能力强|需要安装 C 语言库|
|lxml XML解析器|BeautifulSoup(markup, "xml")|速度快，唯一支持 XML 的解析器|需要安装 C 语言库|
|html5lib|BeautifulSoup(markup, "html5lib")|最好的容错性，以浏览器的方式解析文档，生成 HTML5格式的文档|速度慢，不依赖外部扩展|

### 
### basic using:
```python
from bs4 import BeautifulSoup

with open('test.html', 'r+', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)
out:
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <title>
   Sisters' story
  </title>
 </head>
 <body>
  <p class="title" name="dromouse">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
  </p>
  <a class="sister" href="http://example.com/elsie" id="link1">
   <!--Elsie -->
  </a>
  <a class="sister" href="http://example.com/lacie" id="link2">
   lacie
  </a>
  and
  <a class="sister" href="http://example.com/tillie" id="link3">
   Tillie
  </a>
  <p class="story">
   fdlksjfdkjagldskfkjdasnasknclksdfas...
  </p>
 </body>
</html>
Sisters' story
```
#### using bs4 get some nodes:
```python
from bs4 import BeautifulSoup

with open('test.html', 'r+', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
out:
<title>Sisters' story</title>
<class 'bs4.element.Tag'>
Sisters' story
<head>
<meta charset="utf-8"/>
<title>Sisters' story</title>
</head>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
```
#### using bs4 get node's attrs or attr's value:
```python
from bs4 import BeautifulSoup

with open('test.html', 'r+', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'lxml')
print(soup.title.name)  # get node's name
print(soup.p.attrs)  # get node's attributes
print(soup.p.attrs['name']) # get node's attribute's value
print(soup.p['name'])
print(soup.p['class'])
out:
title
{'class': ['title'], 'name': 'dromouse'}
dromouse
dromouse
['title']
```
#### using bs4 get children nodes or parents nodes and so on:
```python
print(soup.p.string)
print(soup.head.title)
print(type(soup.head.title.string))
print(soup.head.title.string)
print(soup.div.contents)
print(soup.div.children)
for i, child in enumerate(soup.div.children):  # children only foreach every child
    print(i, child)
print(soup.div.descendants)  # generator could foreach every grandson's nodes
for i, child in enumerate(soup.div.descendants):
    print(i, child)
print(soup.a.parent.prettify())
print(list(enumerate(soup.a.parents)))
# get brother nodes
print('Next Sibling', soup.a.next_sibling)
print("Prev Sibling", soup.a.previous_sibling)
print("Next Siblings", list(enumerate(soup.a.next_siblings)))
print("Prev Siblings", list(enumerate(soup.a.previous_siblings)))
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/bs4using.py 
The Dormouse's story
<title>Sisters' story</title>
<class 'bs4.element.NavigableString'>
Sisters' story
['\n', <p class="title" id="dromouse"><b>The Dormouse's story</b></p>, '\n', <p class="story">Once upon a time there were three little sisters; and their names were</p>, '\n', <a class="sister" href="https://example.com/elsie" id="link1"><span>Elsie</span></a>, '\n', <a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a>, ' and\n    ', <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>, '\n', <p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>, '\n']
<list_iterator object at 0x1074a9e80>
0 

1 <p class="title" id="dromouse"><b>The Dormouse's story</b></p>
2 

3 <p class="story">Once upon a time there were three little sisters; and their names were</p>
4 

5 <a class="sister" href="https://example.com/elsie" id="link1"><span>Elsie</span></a>
6 

7 <a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a>
8  and
    
9 <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>
10 

11 <p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>
12 

<generator object Tag.descendants at 0x1074984a0>
0 

1 <p class="title" id="dromouse"><b>The Dormouse's story</b></p>
2 <b>The Dormouse's story</b>
3 The Dormouse's story
4 

5 <p class="story">Once upon a time there were three little sisters; and their names were</p>
6 Once upon a time there were three little sisters; and their names were
7 

8 <a class="sister" href="https://example.com/elsie" id="link1"><span>Elsie</span></a>
9 <span>Elsie</span>
10 Elsie
11 

12 <a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a>
13 <span>lacie</span>
14 lacie
15  and
    
16 <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>
17 <span>Tillie</span>
18 Tillie
19 

20 <p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>
21 fdlksjfdkjagldskfkjdasnasknclksdfas...
22 

<div class="frame">
 <p class="title" id="dromouse">
  <b>
   The Dormouse's story
  </b>
 </p>
 <p class="story">
  Once upon a time there were three little sisters; and their names were
 </p>
 <a class="sister" href="https://example.com/elsie" id="link1">
  <span>
   Elsie
  </span>
 </a>
 <a class="sister" href="https://example.com/lacie" id="link2">
  <span>
   lacie
  </span>
 </a>
 and
 <a class="sister" href="https://example.com/tillie" id="link3">
  <span>
   Tillie
  </span>
 </a>
 <p class="story">
  fdlksjfdkjagldskfkjdasnasknclksdfas...
 </p>
</div>

[(0, <div class="frame">
<p class="title" id="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were</p>
<a class="sister" href="https://example.com/elsie" id="link1"><span>Elsie</span></a>
<a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a> and
    <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>
<p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>
</div>), (1, <body>
<div class="frame">
<p class="title" id="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were</p>
<a class="sister" href="https://example.com/elsie" id="link1"><span>Elsie</span></a>
<a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a> and
    <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>
<p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>
</div>
</body>), (2, <html lang="en">
<head>
<meta charset="utf-8"/>
<title>Sisters' story</title>
</head>
<body>
<div class="frame">
<p class="title" id="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were</p>
<a class="sister" href="https://example.com/elsie" id="link1"><span>Elsie</span></a>
<a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a> and
    <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>
<p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>
</div>
</body>
</html>), (3, <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Sisters' story</title>
</head>
<body>
<div class="frame">
<p class="title" id="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were</p>
<a class="sister" href="https://example.com/elsie" id="link1"><span>Elsie</span></a>
<a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a> and
    <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>
<p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>
</div>
</body>
</html>)]
Next Sibling 

Prev Sibling 

Next Siblings [(0, '\n'), (1, <a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a>), (2, ' and\n    '), (3, <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>), (4, '\n'), (5, <p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>), (6, '\n')]
Prev Siblings [(0, '\n'), (1, <p class="story">Once upon a time there were three little sisters; and their names were</p>), (2, '\n'), (3, <p class="title" id="dromouse"><b>The Dormouse's story</b></p>), (4, '\n')]

Process finished with exit code 0
```
#### using bs4 get info that need:
```python
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(soup.a.parents)
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/bs4using.py 
Next Sibling:
<class 'bs4.element.NavigableString'>




Parent:
<class 'generator'>
<generator object PageElement.parents at 0x104ea44a0>
<div class="frame">
<p class="title" id="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were</p>
<a class="sister" href="https://example.com/elsie" id="link1"><span>Elsie</span></a>
<a class="sister" href="https://example.com/lacie" id="link2"><span>lacie</span></a> and
    <a class="sister" href="https://example.com/tillie" id="link3"><span>Tillie</span></a>
<p class="story">fdlksjfdkjagldskfkjdasnasknclksdfas...</p>
</div>
['frame']

Process finished with exit code 0
```
#### using find or findall get need infos:
##### using name get things:
```python
# using name get things
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
```
##### using attrs get things:
```python
# using attrs get things
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))
```
##### using text get things（Text is a re expression object）:
```python
# using text get things text is a re expression object
print(soup.find_all(text=re.compile('ar')))
```
##### using find method get things(only return first item mathced):
```python
print(soup.find(name='ul'))  # only return first item
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/bs4using.py 
<ul class="list" id="list-1">
<li class="element" name="elements">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<class 'bs4.element.Tag'>
<ul class="list" id="list-1">
<li class="element" name="elements">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>

Process finished with exit code 0
```
#### using CSS Selector get things:
```python
# Css selector
# get element
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
# cycle in cycle
for ul in soup.select('ul'):
    print(ul.select('li'))
# cycle in cycle to get attrs
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
# get text content
for li in soup.select('li'):
    print("Get Text:", li.getText())
    print('String:', li.string)
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/bs4Using.py 
[<div class="panel-heading">
<h4>Hello</h4>
</div>]
[<li class="element" name="elements">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>, <li class="element">Foo</li>, <li class="element" name="elements">Bar</li>]
[<li class="element">Foo</li>, <li class="element" name="elements">Bar</li>]
<class 'bs4.element.Tag'>
[<li class="element" name="elements">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
[<li class="element">Foo</li>, <li class="element" name="elements">Bar</li>]
list-1
list-1
list-2
list-2
Get Text: Foo
String: Foo
Get Text: Bar
String: Bar
Get Text: Jay
String: Jay
Get Text: Foo
String: Foo
Get Text: Bar
String: Bar

Process finished with exit code 0
```
#### bs4 learning End
## pyquery
### simple demo for using pyquery:
```python
import requests
from pyquery import PyQuery as pq
# sample for simply using pyquery
with open('test1.html', 'r+', encoding='utf-8') as f:
    html = f.read()
doc = pq(html)
print(doc('li'))
doc = pq(url='http://www.vincentadamnemessis.site')
print(doc('title'))
doc = pq(requests.get('http://www.vincentadamnemessis.site').text)
print(doc('title'))
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/pyqueryUsing.py 
<li class="element" name="elements">Foo</li>
        <li class="element">Bar</li>
        <li class="element">Jay</li>
      <li class="element">Foo</li>
        <li class="element" name="elements">Bar</li>
      
<title>The Personal Blogs For VincentAdamNemessis</title>&#13;
    
<title>The Personal Blogs For VincentAdamNemessis</title>&#13;
    

Process finished with exit code 0
```
### using pyquery get parents, children or brother nodes or content:
```python
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
lis = items.children()
print(lis)
container = items.parent()
print(type(container))
# print(container)
# print(items.parents())
print(items.siblings())
```
### using pyquery get something and for each:
```python
# for each element
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/pyqueryUsing.py 
<class 'generator'>
<li class="element" name="elements">Foo</li>
         <class 'pyquery.pyquery.PyQuery'>
<li class="element">Bar</li>
         <class 'pyquery.pyquery.PyQuery'>
<li class="element">Jay</li>
       <class 'pyquery.pyquery.PyQuery'>
<li class="element">Foo</li>
         <class 'pyquery.pyquery.PyQuery'>
<li class="element" name="elements">Bar</li>
       <class 'pyquery.pyquery.PyQuery'>

Process finished with exit code 0
```
### using pyquery get information:
```python
# get information
# get attrs and attrs' values
a = doc('.list#list-1')
print(a, type(a))
print(a.attr('data-name'))
print(a.attr.data)
# foreach get items attr's values
a = doc('li')
for item in a.items():
    print(item.attr('class'))
# get text content
a = doc('.list#list-1 .element#selected span')
print(a)
print(a.text())
print(a.html())
li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/pyqueryUsing.py 
<ul class="list" id="list-1" data-name="anyway">
        <li class="element" name="elements">Foo</li>
        <li class="element" id="selected"><span>Bar</span></li>
        <li class="element">Jay</li>
      </ul>
       <class 'pyquery.pyquery.PyQuery'>
anyway
None
element
element
element
element
element
<span>Bar</span>
Bar
Bar
Foo
Foo Bar Jay Foo Bar
<class 'str'>

Process finished with exit code 0
```
### using pyquery change nodes(insert, remove, edit, get):
```python
# nodes action
li = doc('.list#list-1')
print(li)
li.remove_class('list')
print(li)
li.add_class('list4')
print(li)
li.remove_attr('data-name')
print(li)
li.attr('name', 'link')
print(li)
li.text('Changed')
print(li)
li.html('<span>changed item</span>')
print(li)
doc = pq(filename='test1.html')
li = doc('.list#list-1')
li.find('#need').remove()
print(li)
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/pyqueryUsing.py 
<ul class="list" id="list-1" data-name="anyway">
        <li class="element" id="need" name="elements">Foo</li>
        <li class="element" id="selected"><span>Bar</span></li>
        <li class="element">Jay</li>
      </ul>
      
<ul class="" id="list-1" data-name="anyway">
        <li class="element" id="need" name="elements">Foo</li>
        <li class="element" id="selected"><span>Bar</span></li>
        <li class="element">Jay</li>
      </ul>
      
<ul class="list4" id="list-1" data-name="anyway">
        <li class="element" id="need" name="elements">Foo</li>
        <li class="element" id="selected"><span>Bar</span></li>
        <li class="element">Jay</li>
      </ul>
      
<ul class="list4" id="list-1">
        <li class="element" id="need" name="elements">Foo</li>
        <li class="element" id="selected"><span>Bar</span></li>
        <li class="element">Jay</li>
      </ul>
      
<ul class="list4" id="list-1" name="link">
        <li class="element" id="need" name="elements">Foo</li>
        <li class="element" id="selected"><span>Bar</span></li>
        <li class="element">Jay</li>
      </ul>
      
<ul class="list4" id="list-1" name="link">Changed</ul>
      
<ul class="list4" id="list-1" name="link"><span>changed item</span></ul>
      
<ul class="list" id="list-1" data-name="anyway">
        
        <li class="element" id="selected"><span>Bar</span></li>
        <li class="element">Jay</li>
      </ul>
      

Process finished with exit code 0
```
### using pyquery with faked class selector get nodes and so on:
```python
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
out:
/usr/local/bin/python3.9 /Volumes/WorkSpace/ProgramCodes/Python/ParsingLibrariesUsing/pyqueryUsing.py 
<li class="element" id="need" name="elements">Foo</li>
        <li class="element">Foo</li>
        
<li class="element">Jay</li>
      <li class="element" name="elements">Bar</li>
      
<li class="element" id="selected"><span>Bar</span></li>
        <li class="element" name="elements">Bar</li>
      
<li class="element">Foo</li>
        <li class="element" name="elements">Bar</li>
      
<li class="element" id="selected"><span>Bar</span></li>
        <li class="element" name="elements">Bar</li>
      
<li class="element" id="need" name="elements">Foo</li>
        <li class="element">Foo</li>
        

Process finished with exit code 0
```
# The End
# 学习路线与源码已同步 github：[ParsingLibraries基础用法](https://github.com/VincentAdamNemessisX/BasicReptilesParsingLibrariesUsing)
