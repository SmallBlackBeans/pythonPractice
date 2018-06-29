# coding: utf-8

import re
import os
import urllib
from urllib import request


class SpiderTool:
    def __init__(self):
        pass

    # 去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    # 超链接
    removeLink = re.compile('<a.*?>|</a>')
    # 把换行换成\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 把表格制表符<td> 替换成\t
    replaceTD = re.compile('<td>')
    # 把段落替换成\n加空两格
    relacePara = re.compile('<p.*?>')
    # 把换行符或者双换行符替换成\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeLink, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.relacePara, "\n  ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        return x.strip()

    def mkdir(self, path):
        path = path.strip()
        isExists = os.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False

    def saveImg(self, imageURL, filename):
        u = urllib.request.urlopen(imageURL)
        data = u.read()
        f = open(filename, 'wb')
        f.write(data)
        f.close()

    def saveText(self, context, name):
        filename = name + "/" + ".txt"
        f = open(filename, 'w+')
        f.write(context.encode('utf-8'))
