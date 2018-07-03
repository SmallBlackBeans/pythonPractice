# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


# 这些字段用来临时存储你需要保存的数据
import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # 小说名称
    name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 小说链接
    novelurl = scrapy.Field()
    # 连载状态
    serialStatus = scrapy.Field
    # 连载字数
    serialnumber= scrapy.Field()
    # 文章类别
    category = scrapy.Field()
    # 小说标号
    name_id = scrapy.Field()

class DcontentItem(scrapy.Item):
    #小说标号
    id_name = scrapy.Field()
    # 章节内容
    chaptercontent = scrapy.Field()
    # 章节顺序
    num = scrapy.Field()
    # 章节地址
    chapterurl = scrapy.Field()
    # 章节名字
    chaptername = scrapy.Field()
