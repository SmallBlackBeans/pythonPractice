___author__ = 'CQC'
# coding: utf-8

import re

'''
规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑
'''

'''
 • re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
 • re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
 • re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
 • re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
 • re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
 • re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
'''
# r'' 将字符串转换为原生字符串，不用考虑漏写反斜杠
# pattern = re.compile(r"hello(?#我是注释)", re.I)
# result1 = re.match(pattern, 'hello hanchenghai')
# result2 = re.match(pattern, 'helloo hxc')
#
# if result1:
#     print(result1.group())
# else:
#     print('1匹配失败')

# 单词+空格+单词+任意字符
# Match对象是一次匹配的结果
# m = re.match(r'(\w+) (\w+)(?P<sign>(?#组名).*)', 'hello world!')
# print("m.string:", m.string)
# print("m.re:", m.re)
# print("m.pos:", m.pos)
# print("m.endpos:", m.endpos)
# print("m.lastindex:", m.lastindex)
# print("m.lastgroup:", m.lastgroup)
# print("m.group():", m.group())
# print("m.group(1,2):", m.group(1, 2))
# print("m.groups():", m.groups())
# print("m.groupdict():", m.groupdict())
# print("m.start(2):", m.start(2))
# print("m.end(2):", m.end(2))
# print("m.span(2):", m.span(2))
# print(r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3'))  # world hello!


# Search
# pattern = re.compile(r'world')
# match = re.search(pattern,'hello world!')
# if match:
#     print(match.group())


# split 按照能够匹配的子串将string分割后返回列表
# pattern = re.compile(r'\d+')
# group = re.split(pattern, 'one1two2three3four4')
# print(group)


# findAll 以列表形式返回全部能匹配的子串
# pattern = re.compile(r'\d+')
# print (re.findall(pattern, 'one1two2three3four4'))

# finditer 返回一个顺序访问每一个匹配结果（Match对象）的迭代器
# pattern = re.compile(r'\d+')
# for m in re.finditer(pattern, 'one1two2three3four4'):
#     print(m.group())
# ### 输出 ###
# # 1 2 3 4


# sub 单词 + 空格 + 单词 两个组
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(re.sub(pattern, r'\2 \1', s))
# say i, world hello!

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print(re.sub(pattern, func, s))
# I Say, Hello World!

# subn 返回 (sub(repl, string[, count]), 替换次数)



"""零宽断言
?=代表零宽度正预测先行断言，它断言自身出现的位置的后面可以匹配后面跟的表达式。
?<=代表零宽度正回顾后发断言，它断言自身出现的位置的前面可以匹配后面跟的表达式。
?!代表零宽度负预测先行断言，它断言自身出现的位置的后面不可以匹配后面跟的表达式。
?<!代表零宽度负回顾后发断言，它断言自身出现的位置的后面不可以匹配后面跟的表达式。
"""



import re



str = '我的个人邮箱是cqc@cuiqingcai.com，个人博客是cuiqingcai.com，个人公众号是进击的Coder'

# ?=
result = re.search('我的个人邮箱是(.*?)(?=，个人博客)', str)
print('整句结果：' + result.group(), '第一个匹配结果：' + result.group(1), sep='\n')

# ?<=
result = re.search('(?<=，)个人博客是(.*?)(?=，)', str)
print('整句结果：' + result.group(), '第一个匹配结果：' + result.group(1), sep='\n')


# ?!
result = re.search('我的个人邮箱是(.*?)(?!，个人公众号)(?=，个人博客)', str)
print('整句结果：' + result.group(), '第一个匹配结果：' + result.group(1), sep='\n')

# ?<!
result = re.search('(?<=，)(?<!。)个人博客是(.*?)(?=，)', str)
print('整句结果：' + result.group(), '第一个匹配结果：' + result.group(1), sep='\n')



# ，|\Z，意思是匹配逗号或结束符
results = re.findall('个人(.*?)是(.*?)(?=，|\Z)', str)
for result in results:
    print(result[0] + ': ' + result[1])















