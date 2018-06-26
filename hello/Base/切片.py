# coding: utf-8




"""
切片操作返回一个新的 list，不会改变原来 list 的内容
"""

foo = [1, 2, 3, 4, 5, 6]

# 第四个之后的所有元素

bar = foo[3:]

bar = foo[:5]

# 第四个到第六个之间，不包含第六个
bar = foo[3:5]

# 3-5 步长为2
bar = foo[2:5:2]

# 复制一个list
bar = foo[::]

# 反向下标 反转列表
bar = foo[::-1]


# 列表解析
def square_list(list):
    new_elem = [elem ** 2 for elem in list]
    return new_elem


foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bar = [elem for elem in foo if elem % 2 == 0]

# 两个列表的所有元素组合
foo = [1, 3, 5]
bar = [2, 4, 6]
new_list = [(x, y) for x in foo for y in bar]

# 九九乘法表
multiply_list = [','.join(['{0}x{1}={2}'.format(j, i, i * j) for j in xrange(1, i + 1)]) for i in xrange(1, 10)]
