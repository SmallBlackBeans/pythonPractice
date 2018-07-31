# 通过nginx 实现

import requests
from urllib.parse import quote
import re
'''
/usr/local/etc/nginx/nginx.conf
http {
    多个splash服务器地址
    upstream splash {
        least_conn;
        server 41.159.27.223:8050;
        server 41.159.27.221:8050;
    }
    主机监听
    server {
        listen 8050;
        location / {
            proxy_pass http://splash;
            需要权限验证
            auth_basic "Restricted";
            auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
        }
    }
}
权限验证 生成一个用户名为admin的文件
htpasswd -c .htpasswd admin
查看密码 
cat .htpasswd 
重启nginx 服务
sudo ngnix -s reload
'''

lua = '''
function main(splash, args)
  local treat = require("treat")
  local response = splash:http_get("http://httpbin.org/get")
  return treat.as_string(response.body)
end
'''

url = 'http://splash:8050/execute?lua_source=' + quote(lua)
response = requests.get(url, auth=('admin', 'admin'))
ip = re.search('(\d+\.\d+\.\d+\.\d+)', response.text).group(1)
print(ip)