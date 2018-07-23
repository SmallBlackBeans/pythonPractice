from urllib.parse import urlparse,urlencode

'''
解析链接
'''

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result,sep ='\n')


dict = {
    'user':'hanxiaocu',
    'password':'123456'
}

'''
序列化
'''
params = urlencode(dict)
url= 'xxx' + params
print(url)

'''
反序列化
'''
from urllib.parse import parse_qs,parse_qsl
query = 'name=hanxiaocu&age=18'
print(parse_qs(query))
print(parse_qsl(query))


'''
URL编码 / 解码
'''
from urllib.parse import quote,unquote
url = 'xxx' + quote('韩小醋')
print(url)

print(unquote(url))