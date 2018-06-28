import requests
import json
import os
# r = requests.get('http://baidu.com')
# print(type(r))
# # <class 'requests.models.Response'>
# print(r.status_code)
# # 200
# print(r.encoding)
# # ISO-8859-1
# print(r.cookies)
# # <RequestsCookieJar[]>


'''
基本请求
'''

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}

# 表单数据序列化
r = requests.post("http://httpbin.org/post", data=json.dumps(payload))
print(r.text)

# file
url = 'http://httpbin.org/post'
files = {'file':open('test.txt','rb')}
r = requests.post(url,files=files)
print(r.text)

# 文件流式 上传
# with open('massive-body') as f:
#     requests.post('http://some.url/streamed', data=f)


r = requests.get("http://httpbin.org/get", params=payload,headers=headers)
print(r.url)



r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")


r = requests.options("http://httpbin.org/get")

# 网页原始套接字内容
r = requests.get('https://github.com/timeline.json', stream=True)
print(r.raw)


# 超时配置

# 会话对象
s = requests.Session()
s.headers.update({'x-test': 'true'})
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789',headers={'x-test2': 'true'})
r = s.get("http://httpbin.org/cookies")
print(r.text)

# SSL证书验证
r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
print(r.text)


# 代理
proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print(r.text)
