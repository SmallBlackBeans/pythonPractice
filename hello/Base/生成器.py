# coding: utf-8

# generator
# xrange 相比range 生成了一个生成器（ 惰性计算 ），省内存


# 列表解析
foo = [i ** 2 for i in range(10)]
for i in foo:
    print(i)

# 生成器
bar = (i ** 2 for i in range(10))
for i in bar:
    print(i)


# yield 关键字可以让我们的函数变成生成器
# yield 负责将计算的结果放到生成器中
def fib(n):
    index = 0
    f0, f1 = 0, 1
    while index < n:
        yield f0
        f0, f1 = f1, f0 + f1
        index += 1


fib_list = fib(10)
for i in fib_list:
    print(i)

# next() 取生成器生成的值
for i in fib_list:
    print(fib_list.next())


# 迭代器的作用仍然是节省内存 重写 __iter__ 和 next 方法是实现迭代器的协
class Fib(object):
    def __init__(self, n):
        self.f0, self.f1 = 0, 1
        self.index = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        self.index += 1
        if self.index > self.n:
            raise StopIteration

        value = self.f0
        self.f0, self.f1 = self.f1, self.f0 + self.f1
        return value


fib_list = Fib(10)
for i in fib_list:
    print(i)
