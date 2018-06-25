# coding: utf-8

import urllib
from urllib import request
from urllib import parse
from urllib.request import urlopen
import urllib3

url = "http://xxx/login"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'xx', 'password': 'xxx'}
# 对付防盗链，服务器会识别headers中的referer是不是它自己
headers = dict()
headers['User-agent'] = user_agent
headers['Referer'] = "http://www.zhihu.com/articles"
data = parse.urlencode(values).encode(encoding='UTF-8')
req = request.Request(url, data, headers=headers)
res = urlopen(req,timeout=15)
page = res.read()

# Proxy（代理）的设置
enable_proxy = True
proxy_handler = request.ProxyHandler({'http': 'http://some-proxy.com:8080'})
null_proxy_handler = request.ProxyHandler({})
if enable_proxy:
    opener = request.build_opener(proxy_handler)
else:
    opener = request.build_opener(null_proxy_handler)
request.install_opener(opener)



# http协议有六种请求方法，get,head,put,delete,post,options
req = request.Request(url,data=data)
req.get_method = lambda : 'PUT' # or 'DELETE'
res = urlopen(req)

# DebugLog 收发包的内容就会在屏幕上打印出来
httpHandler = request.HTTPHandler(debuglevel=1)
httpsHandler = request.HTTPSHandler(debuglevel=1)
opener = request.build_opener(httpHandler,httpsHandler)
request.install_opener(opener)
urlopen('http://www.baidu.com')


# URLError
url = 'http://www.baidu.com'
req = request.Request(url)
try:
    urlopen(req)
except request.URLError as e:
    print(e.reason)


# HTTPError URLError的子类
# 编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常
try:
    urlopen(req)
except request.HTTPError as e:
    print(e.code)
    print(e.reason)
except request.URLError as e:
    if hasattr(e,'reason'): # 以免出现属性输出报错
        print(e.reason)
else:
    print('OK')