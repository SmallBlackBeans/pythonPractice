# -*- coding: utf-8 -*-

# Scrapy settings for meizi_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meizi_scrapy'

SPIDER_MODULES = ['meizi_scrapy.spiders']
NEWSPIDER_MODULE = 'meizi_scrapy.spiders'

ROBOTSTXT_OBEY = True

IMAGES_STORE = '/Users/hanchenghai/Desktop/meizitu/'
# 过期时间 FILES_EXPIRES (或 IMAGES_EXPIRES) 设置
IMAGES_EXPIRES = 30
# 生成缩略图
# IMAGES_THUMBS = {
#     'small': (50, 50),
#     'big': (270, 270)
# }


# 开启图片下载管道
ITEM_PIPELINES = {
    'meizi_scrapy.pipelines.MeiziScrapyPipeline': 300,
}
# 下载中间件处理
DOWNLOADER_MIDDLEWARES = {
    'meizi_scrapy.middlewares.ImageHotlinkingmiddleware': 543,
    # 'meizi_scrapy.middlewares.UserAgentmiddleware': 400
}
