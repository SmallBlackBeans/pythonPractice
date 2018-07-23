
import os

'''
当搜索爬虫访问一个站点时，它首先会检查这个站点根目录下是否存在robots.txt文件，如果存在，搜索爬虫会根据其中定义的爬取范围来爬取。如果没有找到这个文件，搜索爬虫便会访问所有可直接访问的
'''

# https://www.baidu.com/robots.txt


from urllib.robotparser import RobotFileParser

from urllib.request import urlopen

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')

rp.read()

print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','https://www.jianshu.com/u/40e1253a9808'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))

rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))