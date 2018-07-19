# coding: utf-8


from datetime import datetime,timedelta

from pymongo import MongoClient,errors


class MongoQueue:
    OUTSTANDING = 1 ## 初始状态
    PROCESSING = 2 ## 正在下载中
    COMPLETE = 3 ## 下载完成

    def __init__(self,db,table,timeout=300):
        self.client = MongoClient()
        self.db = self.client[db]
        self.table = self.db[table]
        self.timeout = timeout

