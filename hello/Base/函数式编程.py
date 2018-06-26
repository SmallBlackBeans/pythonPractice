# coding: utf-8
import math

"""
函数式编程 即 把问题抽象成数学公式 然后用编程方式实现
软件工程不存在银弹 没有任何一种模式、范式或者编程方法是万能的，只是对应不同的场景用合适的技术解决问题
"""


# 排序问题之快速排序

# 快速排序过程
# 递归出口是 list 的长度小于等于 1
def qsort_progress(unorder_list):
    # 判断列表长度，如果长度小于 1 直接返回列表本身
    if len(unorder_list) <= 1:
        return unorder_list

    # 获取基准元素
    elem = unorder_list[0]

    # 用列表解析找出所有小于等于基准元素的值存到左边列表中
    left_list = [i for i in unorder_list[1:] if i <= elem]

    # 用列表解析找出所有大于基准元素的值存到右边列表中
    right_list = [i for i in unorder_list[1:] if i > elem]

    # 左边列表继续排序
    sort_left_list = qsort(left_list)

    # 右边列表继续排序
    sort_right_list = qsort(right_list)

    # 返回排好序的结果
    return sort_left_list + [elem] + sort_right_list


# 代码实现
def qsort(unorder_list):
    return qsort([i for i in unorder_list[1:] if i <= unorder_list[0]]) + \
           [unorder_list[0]] + \
           qsort([i for i in unorder_list[1:] if i > unorder_list[0]]) if len(unorder_list) > 1 \
        else unorder_list


print qsort([4, 1, 5, 7, 9, 11, 6])

"""
函数式编程提倡编写纯函数（Pure Function），
纯函数的特点是相同的输入永远返回相同的结果，
这种函数不受外界影响也不会改变外界的状态，
不存在副作用（side effect）
"""

# 匿名函数
anonymous_func = lambda foo: foo + 1

# 高阶函数
# 高阶函数的定义是将函数作为参数的函数，装饰器就是一个高阶函数
N = [1, 2, 3, 4, 5]
S = []
# 命令式
for i in N:
    result = i ** 2
    S.append(result)

# 列表解析
S = [x ** 2 for x in N]

# map
S = map(lambda x: x ** 2, N)

# reduce
n = 5
# 默认从第二个可迭代对象的第一个数据为初始值 即 1 * 1 * 2 * 3 * 4 * 5
result = reduce(lambda x, y: x * y, xrange(1, n + 1))
# 从3 开始 3 * 1 * 2 * 3 * 4 * 5
result = reduce(lambda x, y: x * y, xrange(1, n + 1), 3)

# filter
S = filter(lambda x: x % 2 == 0, N)