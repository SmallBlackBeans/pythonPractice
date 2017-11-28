import  baseHeader

# 多个变量同时赋值
a = b = c = 1

x, y, z = 1, 2, "hanchenghai"

# 标准数据类型
'''
Number 

python3 中只有一种整形类型int  没有了Long
'''

print(type(a), type(c))

print(isinstance(a, str))

'''
isinstance 和 type 的区别
type() 不会认为子类是一种父类类型
isinstance 会认为子类是一种父类类型 多态
'''

# 数值运算

result = 4 // 2  # 整除 2
result2 = 4 / 2  # 2.0

result3 = 2 ** 5  # 乘方32

# 混合运算中 会把整形转换为浮点型

'''
String
Python 没有单独的字符类型，一个字符就是长度为1的字符串

与 C 字符串不同的是，Python 字符串不能被改变。
向一个索引位置赋值，比如word[0] = 'm'会导致错误

+ 连字符 
*5复制当前字符串5次

Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
'''


name = 'hanchenghai'

print(name)
print(name[0:-1])
print(name[0])
print(name[3:len(name)])  # [n:m]不会包含最后一个位置 >=n  <m

# 去掉 转义字符
print(r'我没有转义字符\n')

#

'''
List
与Python字符串不一样的是，列表中的元素是可以改变的：
'''
list1 = [1, 2, 3, 4, 5, 6]
list1[0] = 10
list1[2:5] = [13, 16, 17, 20]  # 替换
print(list1)
list1[2:5] = []  # 删除
print(list1)

'''
Tuple
也可以下标获取

元组的元素不能修改

可以把字符串看作一种特殊的元组
'''
tuple1 = ('a', 1, 2.45, 5)
print(tuple)

tuple2 = ()  # 空元组
print(tuple)
tuple3 = (20,)  # 只有一个元素的元组
print(tuple)

'''
string、list和tuple都属于sequence（序列）
'''

'''
Sets
无序不重复元素的序列
基本功能就是进行成员关系测试和删除重复元素
{} 或者 set()
'''
studens = {'老头', '小黑豆', '吴炎子', '刘新新', '老头'}
print(studens)

m = set('abracadabra')
n = set('alacazaam')

print(m)

# n在m中的相对补集 属于m 不属于n

print(m - n)  # 差集
print(m | n)  # 并集
print(m & n)  # 交集
print(m ^ n)  # 不同时存在的元素

'''
Dictionary
key 必须使用不可变类型：number类型 和 string
'''
# 直接从键值对序列中构建字典
dict1 = dict([('first', 1), ('second', 2), (3, "three")])
print(dict1)
print(dict1.keys())
print(dict1.values())




#Python 3版本中，字符串是以Unicode编码的

print('# 数据类型转换=================')
repr(x)  # 将对象 x 转换为表达式字符串

#eval(name)  # 用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(list1)  # 将序列转换为一个元组
set(list1)  # 转变为可变集合
frozenset(list1)  # 转换为不可变集合
print(chr(65))  # 将编码转换为对应的字符
print(ord('A'))  # 将一个字符转换为它的整数值
hex(x)  # 将一个整数值转换为一个十六进制字符串
oct(x)  # 将一个整数值转换为一个八进制字符串




'''
#字符串类型是str 保存需要转换为bytes
注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
'''
n = b'hanchegnhai'
print(n)
