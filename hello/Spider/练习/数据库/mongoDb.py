# coding: utf-8

from pymongo import MongoClient



client = MongoClient()
db = client['mongoTest']# 数据库 不存在自动创建
meizitu_collection = db['meizitu']# 数据表



