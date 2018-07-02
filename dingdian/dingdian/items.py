# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


# 这些字段用来临时存储你需要保存的数据
import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说名称
    name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 小说链接
    novelUrl = scrapy.Field()
    # 连载状态
    serialStatus = scrapy.Field
    # 连载字数
    serialnumber= scrapy.Field()
    # 文章类别
    category = scrapy.Field()
    # 小说标号
    novel_id = scrapy.Field()
