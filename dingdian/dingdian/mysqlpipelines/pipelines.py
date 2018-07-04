from dingdian.mysqlpipelines.sql import Sql
from dingdian.items import DingdianItem, DcontentItem


class DingdianPipeLine(object):
    def process_item(self, item, spider):
        if isinstance(item, DingdianItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                xs_name = item['name']
                xs_author = item['author']
                category = item['category']
                Sql.insert_dd_name(xs_name, xs_author, category, name_id)
                print('开始存小说标题')

        if isinstance(item, DcontentItem):
            url = item['chapterurl']
            name_id = item['id_name']
            num_id = item['num']
            xs_chaptername = item['chaptername']
            xs_content = item['chaptercontent']
            Sql.insert_dd_chaptername(xs_chaptername, xs_content, name_id, num_id, url)
            print('小说存储完毕')
            return item


from scrapy.pipelines.images import ImagesPipeline


class ImagePipelien(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item


import codecs  # 用法和open相似 区别在于可以处理编码
import json


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('xxx.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 将item写入文件
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


# scrapy 自带类导出json文件
from scrapy.exporters import JsonItemExporter


class JsonExporterPipeline(object):
    def __init__(self):
        self.file = open('xxx.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item=item)
        return item


# mysql
import pymysql
class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='xxx', port='3306', user='root', password='123456', charset='utf-8')
        self.cursor = self.conn.cursor()
    
    def process_item(self,item,spider):
        insert_sql = """INSERT INTO tablename(columnname) VALUES (%s);""" % item['title']
        self.cursor.execute(insert_sql)
        self.conn.commit()

# 连接池
from twisted.enterprise import adbapi
class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_setttings(cls,settings):
        dbparams = dict(host=settings['MYSQL_HOST'], db=settings['MYSQL_DB'], user=settings['MYSQL_USER'],
                 password=settings['MYSQL_PASSWORD'], charset='utf-8', cursorclass=pymysql.cursors.DictCursor,
                 use_unicode=True)
        dbpool = adbapi.ConnectionPool(dbapiName='pymysql',**dbparams)
        return cls(dbpool)

    def process_item(self,item,spider):
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrorback(self.handle_error)

    def handle_error(self,failure):
        print(failure)

    def do_insert(self,cursor,item):
        insert_sql = """INSERT INTO tablename(columnname) VALUES (%s);""" % item['title']
        pass