# coding: utf-8

from pyquery import PyQuery as pq
from lxml import etree

doc = pq("<html></html>")

# 先用lxml 对字符串做补全处理
doc = pq(etree.fromstring("<html></html>"))

doc = pq('http://www.baidu.com')

doc = pq(filename='../lxmlxpath/hello.html')

# print(doc.html())

# print(type(doc))

# li = doc('li')
# print(li.text())
# first item second item third item fourth item fifth item


'''
属性操作
'''
p = pq('<p id="hello" class="hello"></p>')('p')
print(p.attr('id'))
print(p.attr('id', 'plop'))  # 修改id
print(p.attr('id', 'hello'))

print(p.add_class('beauty'))
print(p.remove_class('hello'))
print(p.css('font-size', '16px'))
print(p.css({'background-color': 'yellow'}))

'''
DOM 操作
'''
p = pq('<p id="hello" class="hello"></p>')('p')
print(p.append(' check out <a href="http://www.baidu.com"><span>reddit</span></a>')) # 在最后面追加
print(p.prepend('Oh yes!'))# 在p 最前面追加
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
p.prepend_to(d('#test'))# 把p 加到指定标签位置
print(d)
d.empty() # 清空d的内容
print(d)

'''
遍历
'''
lis = doc('li')
for li in lis.items():
    print(li.html())
# lambda e 变量 冒号后面是表达式
print(lis.each(lambda e: e))


'''
网页请求
'''
print(pq('http://www.baidu.com',headers={'user-agent':'pyquery'}))
print(pq('http://www.baidu.com',{'foo':'bar'},method='post',verify=True))

'''
Ajax
'''