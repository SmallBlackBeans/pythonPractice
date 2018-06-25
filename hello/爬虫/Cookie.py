# coding: utf-8
import urllib
from urllib import parse
from urllib import request
from http import cookiejar  # 2中叫cookielib

#
# cookie = cookiejar.CookieJar()
#
# handler = urllib.request.HTTPCookieProcessor(cookie)
#
# openner = urllib.request.build_opener(handler)
#
# response = openner.open('http://www.baidu.com')
# for item in cookie:
#     print('Name =' + item.name)
#     print('Value =' + item.value)


# 写入文件
# filename = 'cookie.txt'
# cookie = cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# openner = urllib.request.build_opener(handler)
# response = openner.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)


# 从文件读取
# cookie = cookiejar.MozillaCookieJar()
# cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# req = request.Request('http://www.baidu.com')
# opener = request.build_opener(request.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print(response.read())


filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
# HTTPCookieProcessor对象来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = request.build_opener(handler)
pastdata = parse.urlencode({
    'stuid': '201100834510',
    'pwd': '123456'
})
loginUrl = 'login.html'
result = opener.open(loginUrl,pastdata)
cookie.save(ignore_expires=True,ignore_discard=True)
gradeUrl = 'xxx'
result = opener.open(gradeUrl)
print(result)
