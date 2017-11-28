#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

# 多行语句
total = 1 + \
        2 + \
        3
print(total)

"""
多行注释
多行注释
哈哈哈
"""

# 自然字符串 \n会被打印出来 r/R
str = r"this is a line with \n"
print(str)
# unicode字符串 u/U
unicodeStr = u"this is an unicode string"
print(unicodeStr)

# 等待用户输入
# input("你是不是傻")

# 同一行显示多条语句
import  sys;
x = 'hanchenghai'; sys.stdout.write(x + '\n')


# print输出
# 换行
print('nihao')
print('什么👻',end='xxx')
print('oh',end='xxx')

# import 与 from...import
for i in sys.argv:
        print(i)
print('\npython 路径为',sys.path)

from sys import  argv,path  # 导入特定的成员或者函数
print('path:',path)


'''
空值
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。



a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
变量本身类型不固定的语言称之为动态语言

OC动态语言 id类型


swift 一样 当一个变量等于另一个变量时候，是指向了他的数据，但是如果那个数据变化了，那时候才进行数据拷贝，变成两份数据

'''




