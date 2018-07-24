description = '''
全称为Comma-Separated Values，中文可以叫作逗号分隔值或字符分隔值，其文件以纯文本形式存储表格数据
'''

import pandas as pd

import csv


# 写入
with open('data.csv', 'w+', encoding='utf-8') as csvfile:
    # writer = csv.writer(csvfile, dialect='excel', delimiter=' ')
    # writer.writerow(['id', 'name', 'age'])
    # writer.writerow(['10001', 'Mike', 21])
    # writer.writerow(['10002', 'Lily', 22])
    # writer.writerow(['10003', 'Josn', 23])
    # # 写入多行
    # writer.writerows([['10004', 'Josn', 24], ['10005', 'Josn', 25], ['10006', 'Josn', 26]])

    # 写入字典
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'mike1', 'age': 21})
    writer.writerow({'id': '10002', 'name': 'mike2', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'mike3', 'age': 23})


# 读取
with open('data.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)



df = pd.read_csv('data.csv')
print(df)