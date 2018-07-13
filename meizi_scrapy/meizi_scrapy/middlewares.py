# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html




'''
中间件处理图片下载的防盗链
'''
class ImageHotlinkingmiddleware(object):
    def process_request(self,request,spider):
        referer = request.meta.get('referer',None)
        if referer:
            request.headers['referer'] = referer
        else:
            request.headers['referer'] = 'http://i.meizitu.net'


import random
from .useragent import agents
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
'''
代理
'''
class UserAgentmiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers['User-Agent'] = agent