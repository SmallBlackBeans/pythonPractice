import pymysql

db = pymysql.connections.Connection(host='localhost', user='root', password='123456', port='3306')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('DataBase version:', data)

cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER set utf8")
db.close()
