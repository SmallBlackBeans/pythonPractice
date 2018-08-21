# -*- coding: utf-8 -*-

"""
    @Time    : 2018/8/21 上午11:04
    @Author  : hanxiaocu
    @File    : tools.py

    数据库存储
"""

import pymysql.cursors


class DBToMysql():

    def __init__(self, configs):
        self.configs = configs

    def start_conn(self):
        '''建立连接'''
        self.conn = pymysql.connections.Connection(cursorclass=pymysql.cursors.DictCursor,
                                                   host=self.configs['host'], user=self.configs['user'],
                                                   password=self.configs['password'], db=self.configs['db'],
                                                   charset='utf8mp4', )

    def close(self):
        '''关闭数据库'''
        self.conn.close()

    def save_one_data(self, table, data, ):
        '''
        将一条数据保存
        :param table: 表名
        :param data: 一条记录
        :return:
            成功：dict
            失败：-1
        '''
        self.start_conn()
        key_map = {}
        if len(data) == 0:
            return -1
        fields = ''
        values = ''

        datas = {}
        for k, v in data.items:
            # 防止sql注入 对值进行转码
            datas.update({k: pymysql.escape_string(v)})

        for d in datas:
            fields += "`{}`,".format(str(d))
            values += "`{}`,".format(str(data[d]))

        if len(fields) <= 0 or len(values) <= 0:
            return -1

        sql = "insert ignore into {}({}) values ({})".format(table, fields[:-1], values[:-1])

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                self.conn.commit()
                cursor.close()
        except Exception as e:
            print(e)
        self.close()

    def find_all(self, table, limit=-1):
        '''
        查询所有的记录
        :param table:
        :param limit:
        :return:
        '''
        try:
            self.start_conn()
            with self.conn.cursor() as cursor:
                if limit == -1:
                    sql = "select * from {}".format(table)
                else:
                    sql = "select * from {} limit 0,{}".format(table, limit)
                cursor.execute(sql)
                res = cursor.fetchall()
                return res
        except Exception as e:
            print('数据查询错误')
            return -1
        finally:
            self.close()

    def find_by_field(self, table, field, field_value):
        '''
        指定条件查询
        :param table:
        :param field:
        :param field_value:
        :return:
        '''
        try:
            self.start_conn()
            with self.conn.cursor() as cursor:
                sql = "select * from {} where {} = '{}'".format(
                    table, field, field_value
                )
                cursor.execute(sql)
                res = cursor.fetchall()
                return res
        except Exception as e:
            print('条件查询错误')
            return -1
        finally:
            self.close()

    def find_by_fields(self, table, queryset={}):
        try:
            self.start_conn()
            with self.conn.cursor() as cursor:
                querys = ""
                for k, v in queryset.items():
                    querys += "{} = '{}' and ".format(k, v)
                sql = "select * from {} where {}".format(
                    table, querys[:-4]  # 去掉最后一个and
                )
                cursor.execute(sql)
                res = cursor.fetchall()
                return res

        except Exception as e:
            print('条件查询失败')
            return -1
        finally:
            self.close()

    def find_by_sort(self, table, field, limit=1000, order='DESC'):
        '''排序'''

        try:
            self.start_conn()
            with self.conn.cursor() as cursor:
                sql = "select * from {} order by {} {} limit 0, {}".format(
                    table, field, order, limit
                )
                cursor.execute(sql)
                res = cursor.fetchall()
                return res
        except Exception as e:
            print('排序查询失败')
            return -1
        finally:
            self.close()
















