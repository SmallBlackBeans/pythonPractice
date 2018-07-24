import json

# 请千万注意JSON字符串的表示需要用双引号
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
#
# print(str)
# data = json.loads(str)
# print(data)
# print(type(data))
#
# data[0]['name']
# # 推荐使用get()方法，这样如果键名不存在，则不会报错 会返回None 而且get 还可以传入默认值
# data[0].get('name')


data = None
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

# json -> 字符串
with open('data.json', 'w') as file:
    # ensure_ascii 处理中文
    file.write(json.dumps(data,indent=2,ensure_ascii=False))
