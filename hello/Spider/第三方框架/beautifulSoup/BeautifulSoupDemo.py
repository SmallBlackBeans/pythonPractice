# coding: utf-8

import bs4
from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

# print(soup.prettify())
#
# # NavigableString
# print(soup.p.string)
#
# # Comment 注释
# if type(soup.a.string) == bs4.element.Comment:
#     print(soup.a.string)
#

'''
文档树
'''
# # .contents 子节点列表
#
# .chirldren 一个list生成器
# for child in  soup.body.children:
#     print(child)

# # .descendants 所有的子孙节点
# for child in soup.descendants:
#     print(child)

#  .strings  .stripped_strings 属性
# for string in soup.strings:
#     # print(repr(string))

# 可以去除多余空白内容
# for string in soup.stripped_strings:
#     print(repr(string))

'''
搜索文档树  find_all( name , attrs , recursive , text , **kwargs )
'''
"""
1）name 参数
"""
# 传字符串
content = soup.find_all('a')
print(content)

# 传正则表达式
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

# 传列表
soup.find_all(["a", "b"])

# 传 True 查找到所有的tag,但是不会返回字符串节点
for tag in soup.find_all(True):
    print(tag.name)
# 传方法 如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)

"""
2）keyword 参数
"""
soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
soup.find_all(href=re.compile("elsie"))

soup.find_all(href=re.compile("elsie"), id='link1')

#  class 是 python 的关键词
soup.find_all("a", class_="sister")


data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={"data-foo":"value"})

"""
3）text 参数
"""
soup.find_all(text=["Tillie", "Elsie", "Lacie"])

"""
4）limit 参数 类似sql 中的limit
"""
soup.find_all("a", limit=2)

"""
5）recursive 参数 是否递归检索子节点
"""
soup.html.find_all("title", recursive=False)


'''
CSS选择器 返回数组
'''
# 标签名
soup.select('title')
# class
soup.select('.sister')
# id
soup.select('#link')
# 组合查找
soup.select('p #link')
# 子标签
soup.select('head > title')
# 属性
soup.select('a[class="sister"]')
soup.select('a[href="http://example.com/elsie"]')
for title in soup.select('title'):
    print(title.get_text())

