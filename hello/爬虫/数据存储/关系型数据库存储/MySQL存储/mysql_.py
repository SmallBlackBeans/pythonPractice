import pymysql
import random

import logging

logger = logging.getLogger(__name__)

db = pymysql.connections.Connection(
    host='127.0.0.1',
    user='root',
    password='Mysql@Han0302',
    port=3306,
    charset='UTF8MB4',
    db='spiders')

cursor = db.cursor()

# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('DataBase version:', data)

# 创建数据库
cursor.execute("CREATE DATABASE IF NOT EXISTS spiders DEFAULT CHARACTER set UTF8MB4")

# 创建数据库表
sql = "CREATE TABLE IF NOT EXISTS students (id varchar(255) not null ,name varchar(255) not null ,age int not null ,primary key (id))"
cursor.execute(sql)

table = 'students'


# 插入数据
def insert():
    data = {
        'id': '201100834511' + str(int(random.random() * 10)),
        'name': 'hanxiaocu',
        'age': random.random() * 1000 % 30
    }
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('插入成功')
            db.commit()
    except:
        print('插入失败')
        db.rollback()


# 更新数据
def update():
    sql = 'UPDATE {table} SET age=%s WHERE name = %s'.format(table=table)
    try:
        print('更新成功')
        cursor.execute(sql, (25, 'Bob'))
        db.commit()
    except:
        print('更新失败')
        db.rollback()


# 更新去重 如果主键已经存在，就执行更新操作 不存在就执行插入
def duplicate():
    data = {
        'id': '201100834511' + str(int(random.random() * 10)),
        'name': 'hanxiaocu',
        'age': random.random() * 1000 % 30
    }
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys,
                                                                                          values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    sql += update

    try:
        if cursor.execute(sql, tuple(data.values()) * 2):
            print('去重更新/插入成功')
            db.commit()
    except:
        print('去重更新/插入失败')
        db.rollback()


# 删除
def delete():
    condition = 'age > 25'
    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)

    try:
        if cursor.execute(sql):
            print('删除成功')
            db.commit()
    except:
        db.rollback()


# 查询
def select():
    try:
        sql = 'select * from students where age >= 15'
        cursor.execute(sql)
        print('Count: ', cursor.rowcount)
        row = cursor.fetchone()
        # results = cursor.fetchall()
        # print('Results: ', results)
        # print('Results Type: ', type(results))
        # for row in results:
        #     print(row)
        while row:
            print('Row: ',row)
            row = cursor.fetchone()
    except:
        print('Error')


for i in range(10):
    import time
    # time.sleep(0.2)
    duplicate()

# update()
# delete()
select()
db.close()
