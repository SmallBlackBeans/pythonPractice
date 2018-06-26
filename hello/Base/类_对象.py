# -*- coding:UTF-8 -*-

"""
    OOP 具有继承（Inherit）多态（Polymorphism）和封装（Encapsulation）三个特点。
"""


class Girl(object):

    # Python 中变量和方法前加两个下划线 __ 表示 private，一个下划线 _ 表示 protect，不加表示 public

    # 避免上帝类 啥都让他干了
    def __init__(self, skin, character, good_at):
        self.skin = skin
        self.character = character
        self.good_at = good_at

    def sayHello(self):
        print("hello")

    def show(self):
        print("I am good at %s" % self.good_at)



