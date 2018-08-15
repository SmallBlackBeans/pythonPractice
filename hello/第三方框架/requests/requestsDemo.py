import requests
import json
import os

r = requests.get('http://baidu.com')
print(type(r))
# <class 'requests.models.Response'>
print(r.status_code)
# 200
print(r.encoding)
# ISO-8859-1
#从内容分析编码类型
print(r.apparent_encoding)
# 二进制
print(r.content)

'''
cookies
'''
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)

# <RequestsCookieJar[]>


'''
基本请求
'''

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}

# 表单数据序列化
r = requests.post("http://httpbin.org/post", data=json.dumps(payload))
print(r.text)

'''
文件上传
'''
url = 'http://httpbin.org/post'
files = {'file': open('test.txt', 'rb')}
r = requests.post(url, files=files)
print(r.text)

'''
 文件流式 上传
'''
with open('massive-body') as f:
    requests.post('http://some.url/streamed', data=f)

r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
print(r.url)

r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")

r = requests.options("http://httpbin.org/get")

# 网页原始套接字内容
r = requests.get('https://github.com/timeline.json', stream=True)
print(r.raw)


'''
会话对象
'''
s = requests.Session()
s.headers.update({'x-test': 'true'})
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789', headers={'x-test2': 'true'})
r = s.get("http://httpbin.org/cookies")
print(r.text)

# 构造Request
request = requests.Request(url,data=None,headers=None)
prepped = s.prepare_request(request)
r = s.send(prepped)


'''
SSL证书验证
'''
import urllib3
import logging
urllib3.disable_warnings() # 屏蔽警告⚠️
logging.captureWarnings(True) # 或者捕获警告道日志的方式起来忽略警告
r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
print(r.text)


'''
 代理设置
'''
proxies = {
    "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print(r.text)

'''
超时配置
'''
r = requests.get("https://www.taobao.com", timeout = 1)

'''
身份认证
'''
from requests.auth import HTTPBasicAuth
r = requests.get(url,auth=HTTPBasicAuth('username','password'))
print(r.status_code)

'''
状态码
'''
from requests import codes, status_codes

r = requests.get('http://baidu.com')
exit() if not r.status_code == requests.codes else print('Request Successfully')
