#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# 文件名 helloworld.py



print("你好")

# 注释

name = "hanchenghai" #这是一个注释
print(name)



# input("\n\nPress the enter key to exit")


import  sys;
x = 'runoob';
sys.stdout.write(x + '\n')
x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)
print('=======')
#不换行输出
print(x,)
print(y,)


if x == y :
    print('haha')
elif x == y :
    print('xixi')
else:
    print('hohou')


counter = 1000
miles = 1000.0
name = "Jone"


print(counter)
print(miles)
print(name)

a = b = c = 1
a, b, c = 1, 2, "jomne"
print(a, b, c)

# 五个标准的数据类型
'''
Numbers 
 int long float complex(a,b) a+bj 复数 a,b都是浮点型

String List Tuple Dictionary
'''
num1 = 1
num2 = 10
#删除对象的引用
del num1
del num2


s = 'Iloveyou'
print(s[1:5])#包含1 不包含5


str = 'hello world!'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + 'test')

# List
list = ['runnob', 789, 2.24, 'jone', 4848]
tinylist = [123, 'jone']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

# 元组 不能二次赋值，相当于只读列表
tuple = ('runnob', 789, 2.33, 'jone', 56)
tinyTuple = (123, "jome")
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinyTuple * 2)
print(tuple + tinyTuple)

# tuple[2] = 1000 'tuple' object does not support item assignment


# 字典
dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"
tinydict = {'name':'jone', 'code':444, 'dept':'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())


#数据类型转换



# 算术运算符
a = 10
b = 2
a**b #幂次方 10^2

9//2#4  取整除 返回商的整数部分
9.0//2.0#4.0

#比较运算符
print(a==b)
print(a!=b)

#赋值运算符
c = a + b
c+=a
c**=a
c//=a
#位运算符
a = 60; b = 13
#a = 00111100 ; b = 00001101

#按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
print(a&b)#00001100
#按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
print(a|b)#00111101
#按位异或运算符：当两对应的二进位相异时，结果为1
print(a^b)#00110001
#按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
print(~a)#11000011
#左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0
print(a<<2)
#右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
print(a>>2)

#逻辑运算符
a = 10
b = 20
if (a and b):#布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值
    print("1 - 变量a 和 b 都为 true")
else:
    print("1 - 变量a 和 b 有一个不为true")

print(a and b)#20

# 成员运算符
list = [1, 2, 3, 4, 5]
if (a in list):
    print("变量a 在list列表中")
else:
    print("没有在list 列表中找到a变量")

if (b not in list):
    print("变量b不在给定的list中")
else:
    print("变量b在给定的列表list中")


# 身份运算符 is / is not
if (a is b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有指向同一个地址")

print(id(a))#4408632704
print(id(b))#4408633024


'''
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''

a = [1, 2, 3]
b = a
print(b is a)
print(a == b)
b = a[:]#下标取值 类似于swift的片段，生成新的一个变量
print(b)
print(b is a)
print(a == b)

#运算符优先级(由高到低)
'''
** 指数
~ + - (按位翻转 一元加号 一元减号)
* / % //®
+ - 
<<  >>
& 位 'AND'
^ | 位运算
<= < > >=
== !=
=   %=  /=  //= -= += *= **= 
is is not
in not in
not or and
'''


'''
Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
python 没有 switch 语句
'''
num = 10
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print("hello")
else:
    print("undefine")

var = 100
if (var == 100) : print("hahahha")

numbers = [12, 27, 55, 15, 88, 3]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

print(even)
print(odd)


var = 1
while var == 1:
    num = input("请输入一个数字:")
    print("你输入的是:",num)
    if (int(num) % 2 == 0):
        break

print("拜拜")

count = 0
while count < 5:
    count += 1
    print(count)
else:
    print("超过了5了")



#多行语句
total = 1 + \
        2 + \
        3

print(total)