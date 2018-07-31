# Splash是一个JavaScript渲染服务，是一个带有HTTP API的轻量级浏览器

"""
异步方式处理多个网页渲染过程；
获取渲染后的页面的源代码或截图；
通过关闭图片渲染或者使用Adblock规则来加快页面渲染速度；
可执行特定的JavaScript脚本；
可通过Lua脚本来控制页面渲染过程；
获取渲染的详细过程并通过HAR（HTTP Archive）格式呈现


Splash 是通过Lue脚本控制的页面加载过程，模拟浏览器
"""

import requests
# url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
# response = requests.get(url)
# print(response.text)
#
# url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
# response = requests.get(url)
# with open('jd.png', 'wb') as f:
#     f.write(response.content)


# 和Lua交互
from urllib.parse import quote

lua = '''
function main(splash, args)
  local treat = require("treat")
  local response = splash:http_get("http://httpbin.org/get")
    return {
    html=treat.as_string(response.body),
    url=response.url,
    status=response.status
    }
end
'''
# quote URL转码
url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
resonse = requests.get(url)
print(resonse.text)
