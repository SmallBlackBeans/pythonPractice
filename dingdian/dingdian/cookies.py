import requests
import json
import redis
import logging
from .settings import REDIS_URL


logger = logging.getLogger(__name__)
## 使用REDIS_URL链接Redis数据库, deconde_responses=True这个参数必须要，数据会变成byte形式 完全没法用
reds = redis.Redis.from_url(REDIS_URL,db=2,decode_responses=True)
login_url = 'http://handuofuli.pw/wp-login.php'

def get_cookies(account,password):
    s = requests.Session()
    payload = {
        'log':account,
        'pwd':password,
        'rememberme':'forever',
        'wp-submit':'登录',
        'redirect_to':'http://www.haoduofuli.pw/wp-admin/',
        'testcookie':'1'
    }
    response = s.post(login_url,data=payload)
    cookies = response.cookies.get_dict()
    logger.warning('获取cookies 成功,账号为%s' % account)
    # 如果不序列化，存入Redis后会变成Plain Text格式的
    return json.dumps(cookies)

def init_cookie(red,spidername):
    redkeys = reds.keys()
    for user in redkeys:
        password = reds.get(user)
        if red.get("%s:Cookies:%s--%s" % (spidername,user,password)) is None:
            cookie = get_cookies(user,password)
            red.set("%s:Cookies:%s--%s" % (spidername,user,password),cookie)


def update_cookie(red,accountText,spidername):
    red = redis.Redis()
    pass

def remove_cookie(red:redis.Redis,spidername,accountText):
    red.delete("%s:Cookies:%s" % (spidername,accountText))