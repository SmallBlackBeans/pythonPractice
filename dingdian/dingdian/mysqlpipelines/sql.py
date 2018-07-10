# mysql


import mysql.connector
from dingdian import settings

MYSQL_HOST = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

# 建立连接上下文
cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, database=MYSQL_DB)
# 游标
cur = cnx.cursor(buffered=True)


class Sql:

    @classmethod
    def insert_dd_name(cls, xs_name, xs_author, category, name_id):
        sql = 'INSERT  INTO dd_name(`xs_name`, `xs_author`,`category`, `name_id`) VALUES (%(xs_name)s,%(xs_author)s,%(category)s,%(name_id)s)'
        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'category': category,
            'name_id': name_id
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_name(cls, name_id):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def insert_dd_chaptername(cls, xs_chaptername, xs_content, id_name, num_id, url):
        sql = 'INSERT INTO dd_chaptername(`xs_chaptername`,`xs_content`,`id_name`,`num_id`, `url`)' \
              'VALUES (%(xs_chaptername)s,%(xs_content)s,%(id_name)s,%(num_id)s,%(url)s)'
        value = {
            'xs_chaptername': xs_chaptername,
            'xs_content': xs_content,
            'id_name': id_name,
            'num_id': num_id,
            'url': url
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_chapter(cls, url):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_chaptername WHERE url=%(url)s)"
        value = {
            'url': url
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]


    '''
    一个SQL脚本
    '''
    # def process_item(self, item, spider):
    #     if isinstance(item, WhoscoredNewItem):
    #         table_name = item.pop('table_name')
    #         col_str = ''
    #         row_str = ''
    #         for key in item.keys():
    #             col_str = col_str + " " + key + ","
    #             row_str = "{}'{}',".format(row_str, item[key] if "'" not in item[key] else item[key].replace("'", "\\'"))
    #             sql = "insert INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE ".format(table_name, col_str[1:-1], row_str[:-1])
    #         for (key, value) in six.iteritems(item):
    #             sql += "{} = '{}', ".format(key, value if "'" not in value else value.replace("'", "\\'"))
    #         sql = sql[:-2]
    #         self.cursor.execute(sql) #执行SQL
    #         self.cnx.commit()# 写入操作