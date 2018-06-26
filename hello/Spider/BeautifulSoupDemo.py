# coding: utf-8

import bs4
from bs4 import BeautifulSoup

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
# ## 文档树
# # .contents 子节点列表
#
# .chirldren 一个list生成器
# for child in  soup.body.children:
#     print(child)

# # .descendants 所有的子孙节点
for child in soup.descendants:
    print(child)