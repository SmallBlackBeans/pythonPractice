# encoding: utf-8

def foo(bar, a=1, *args, **kwargs):
    # çargs 数组 kwargs 字典
    print(bar)
    print(a)
    print(args)
    print(kwargs)


foo('韩小醋', 3, 1, 2, 5, c=7, d=8)


dict = {'1':'nihao','2':'en','3':'hah'}

for d in dict:
    print(d)
