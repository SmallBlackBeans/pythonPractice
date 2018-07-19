# coding: utf-8


from lxml import etree


text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

# html
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result)

# 本地解析 parse
from lxml import etree
html = etree.parse('hello.html')
result = etree.tostring(html,pretty_print=True)
print(result)

'''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# 查找所有的li 标签
result = html.xpath('//li')
result = html.xpath('//li/@class')

result = html.xpaht('//li/a[@href="link1.html"]')

# 这里不能使用单斜杠 因为span 不是li的子元素
result = html.xpath('//li//span')

result= html.xpath('//li/a//@class')
# ['blod']

result = html.xpath('//li[last()]/a/@href')

result = html.xpath('//*[@class="bold"]')