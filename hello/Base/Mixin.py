# coding: utf-8

import os;

"""
    继承的缺点是是这种模式使得类之间的耦合度很高
    组合的好处是降低了类与类之间的耦合程度
    Mixin不同于组合方式，Mixin 使用多继承来达到组合的目的,类似于swift中的多协议
"""


class Staff(object):
    '''
    员工类
    '''
    def __init__(self,gender, work_years):
        self.work_years = work_years
        self.gender = gender

