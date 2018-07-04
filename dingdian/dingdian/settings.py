# -*- coding: utf-8 -*-

# Scrapy settings for dingdian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dingdian'

SPIDER_MODULES = ['dingdian.spiders']
NEWSPIDER_MODULE = 'dingdian.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'dingdian (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# 最大请求数 默认16
# CONCURRENT_REQUESTS = 32

'''
http cache
'''
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



'''
redis
'''
# 启用redis 调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 确保所有的爬虫通过redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 默认请求序列化使用的是pickle 但是我们可以更改为其他类似的。PS：这玩意儿2.X的可以用。3.X的不能用
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# 不清除Redis队列、这样可以暂停/恢复 爬取
# SCHEDULER_PERSIST = True

# 使用优先级调度请求队列 （默认使用）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 可选用的其它队列
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# 最大空闲时间防止分布式爬虫因为等待而关闭
# 这只有当上面设置的队列类是SpiderQueue或SpiderStack时才有效
# 并且当您的蜘蛛首次启动时，也可能会阻止同一时间启动（由于队列为空）
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 序列化项目管道作为redis Key存储
# REDIS_ITEMS_KEY = '%(spider)s:items'

# 默认使用ScrapyJSONEncoder进行项目序列化
# You can use any importable path to a callable object.
# REDIS_ITEMS_SERIALIZER = 'json.dumps'

# 指定连接到redis时使用的端口和地址（可选）
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379

# 指定用于连接redis的URL（可选）
# 如果设置此项，则此项优先级高于设置的REDIS_HOST 和 REDIS_PORT
REDIS_URL = 'redis://root:123456@localhost:6379'

# 自定义的redis参数（连接超时之类的）
# REDIS_PARAMS  = {}

# 自定义redis客户端类
# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# 如果为True，则使用redis的'spop'进行操作。
# 如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
# REDIS_START_URLS_AS_SET = False

# RedisSpider和RedisCrawlSpider默认 start_usls 键
# REDIS_START_URLS_KEY = '%(name)s:start_urls'

# 设置redis使用utf-8之外的编码
# REDIS_ENCODING = 'latin1'


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700
}

ITEM_PIPELINES = {
    # 后面的 1 是优先级程度（1-1000随意设置，数值越低，组件的优先级越高）
    'dingdian.mysqlpipelines.pipelines.DingdianPipeLine': 1,
    # 'dingdian.pipelines.DingdianPipeline': 300,
    # 用Redis处理结果
    'scrapy_redis.pipelines.RedisPipeline': 300,
    # 'scrapy.pipelines.images.ImagePipeline': 1
    'dingdian.mysqlpipelines.pipelines.ImagePipeline': 1,
    # json
    'dingdian.mysqlpipelines.pipelines.JsonWithEncodingPipeline': 2,
}

'''
图片下载处理
'''
import os

project_dir = os.path.abspath(os.path.dirname(__file__))
IMAGE_STORE = os.path.join(project_dir, 'images')
# 用于过滤小图片
IMAGE_MIN_HEIGHT = 100
IMAGE_MIN_WIDTH = 100


'''
mysql
'''
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = '3306'
MYSQL_DB = 'dingdianxiaoshuo'
