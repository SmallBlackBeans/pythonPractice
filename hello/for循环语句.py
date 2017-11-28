#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
for letter in "Python":
    print("当前字母:", letter)

fruits = ["老头子", "小黑豆", "吴彦祖"]

#  range返回一个序列的数 0 - 3
for index in range(len(fruits)):
    print("当前水果:" + fruits[index])

# 获取质数
for num in range(10, 100):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d 等于 %d * %d" % (num, i, j))
            break
    else:
        print(num, "是一个质数")

# 获取100以内的素数(质数)
i = 2
while i < 100:
    j = 2
    while float(j) <= i / j:
        if not (i % j): break
        j = j + 1
    if i / j < float(j): print(i, "是素数")
    i = i + 1


