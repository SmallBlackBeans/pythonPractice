# coding: utf-8

# MRO（Method Resolution Order） 方法解析顺序



class A(object):
    def eat(self):
        print('A eat')


class B(A):
    pass


class C(A):
    def eat(self):
        print('C eat')


class D(B, C):
    pass


print(D.__mro__)


# super 函数
class Employee(object):
    """
    普通员工
    """

    def __init__(self):
        print('I am a employee')

class Programmer(Employee):
    """
    程序员
    """
    def __init__(self):
        print('I am a Programmer')
        super(Programmer,self).__init__()
        print('I  use python')

class OPS(Employee):
    """
    运维
    """
    def __init__(self):
        print('I am  a  dev ops')
        super(OPS,self).__init__()
        print('I can monitor all service')

class CTO(Programmer,OPS):
    def __init__(self):
        print('I am a cto')
        super(CTO,self).__init__()
        print(" 啥都会")