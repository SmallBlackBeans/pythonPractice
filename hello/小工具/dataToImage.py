# -*- coding: utf-8 -*-

"""
    @Time    : 2018/9/30 11:29 AM
    @Author  : hanxiaocu
    @File    : dataToImage.py
    
    
"""
import base64

def dateToimage():
    data = ""
    imgdata=base64.b64decode(data)
    file=open('2.jpg','wb')
    file.write(imgdata)
    file.close()



def imageToData():
    f=open('723.png','rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    f.close()
    print(ls_f)


if __name__ == '__main__':
    dateToimage()