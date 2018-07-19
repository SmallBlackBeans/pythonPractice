# coding: utf-8

import time
import pymysql

# http://www.runoob.com/python3/python3-mysql.html
ANSWER_TABLE_NAME = "answer_table"
QUESTIONS_TABLE_NAME = "questions_table"

"""
CREATE TABLE IF NOT EXISTS `answer_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `text` text NOT NULL COMMENT '回答内容',
  `question_id` int(18) NOT NULL COMMENT '问题ID',
  `answerer` varchar(255) NOT NULL COMMENT '回答者',
  `date` varchar(255) NOT NULL COMMENT '回答时间',
  `is_good` int(11) NOT NULL COMMENT '是否是最佳答案',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
 
CREATE TABLE IF NOT EXISTS `questions_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '问题ID',
  `text` text NOT NULL COMMENT '问题内容',
  `questioner` varchar(255) NOT NULL COMMENT '提问者',
  `date` date NOT NULL COMMENT '提问时间',
  `ans_num` int(11) NOT NULL COMMENT '回答数量',
  `url` varchar(255) NOT NULL COMMENT '问题链接',
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
"""


class Mysql:
    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    def __init__(self):
        try:
            self.db = pymysql.Connect('127.0.0.1', 'test', 'root', '123456')
            self.cur = self.db.cursor()
        except pymysql.Error as e:
            print(self.getCurrentTime(), "连接数据库错误，原因%d: %s" % (e.args[0], e.args[1]))


    def insertData(self, table, data_dict: dict):
        try:
            self.db.set_charset('utf-8')
            cols = ', '.join(data_dict.keys())
            values = '"," '.join(data_dict.values())
            sql = "INSERT INTO " + ANSWER_TABLE_NAME + " (%s) VALUES (%s)" % (cols, '"' + values + '"')
            print("插入语句 " % sql)
            try:
                result = self.cur.execute(sql)
                insert_id = self.db.insert_id()
                self.db.commit()
                if result:
                    return insert_id
                else:
                    return 0
            except pymysql.Error as e:
                self.db.rollback()
                if "key 'PRIMARY" in e.args[1]:
                    print(self.getCurrentTime(), "数据库插入失败")
                else:
                    print(self.getCurrentTime(), "插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
        except pymysql.Error as e:
            print(self.getCurrentTime(), "数据库错误，原因%d: %s" % (e.args[0], e.args[1]))
