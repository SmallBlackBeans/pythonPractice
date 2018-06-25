# coding: utf-8


import urllib
from urllib import request
import re

page = 1

url = "http://www.qiushibaike.com/hot/page/" + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
'''
<div class="article block untagged mb15 typs_long" id="qiushi_tag_120595708">
'''
try:
    print("begin")
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<a.*?<h2>(.*?(?#用户姓名))</h2>.*?<span>(.*?(?#内容))</span>', re.S)
    # re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。
    items = re.findall(pattern, content)
    for item in items:
        print(items[0], items[1])
    print("end")
except urllib.request.HTTPError as e:
    print(e.reason)
except urllib.request.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
except Exception as e:
    print(e)
