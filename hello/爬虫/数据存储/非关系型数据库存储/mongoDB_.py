import pymongo
from pymongo import collection

client = pymongo.MongoClient(host='localhost', port=27017)

# client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['test']

stuCollection: collection.Collection = db['students']

student = {
    'id': '111',
    'name': 'hanxiaocu',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '112',
    'name': 'xiaoheidou',
    'age': 26,
    'gender': 'male'
}

# 插入
result = stuCollection.insert_many([student, student2])
print(result)
print(result.inserted_ids)

# 查询
result = stuCollection.find_one({'name': 'xiaoheidou'})
# print(type(result))
# print(result)

from bson.objectid import ObjectId

result = stuCollection.find_one({'_id': ObjectId('5b582447c7cf384e90ae1495')})
print(result)

results = stuCollection.find({'age': 20})
# 返回结果是Cursor类型，它相当于一个生成器
for result in results:
    print(result)

# 条件查询
results = stuCollection.find({'age': {'$gt': 20}})
results = stuCollection.find({'age': {'$in': [10, 30]}})

# 功能符号 如 正则
'''
$regex   匹配正则表达式
{'name': {'$regex': '^M.*'}}   name以M开头

$exists  属性是否存在 
{'name': {'$exists': True}}    name属性存在

$type    类型判断 
{'age':  {'$type': 'int'}}     age的类型为int

$mod     数字模操作     
{'age': {'$mod': [5, 0]}}      年龄模5余0

$text    文本查询
{'$text': {'$search': 'Mike'}} text类型的属性中包含Mike字符串

$where高级条件查询
{'$where': 'obj.fans_count == obj.follows_count'}  自身粉丝数等于关注数
'''
results = stuCollection.find({'name': {'$regex': '^M.*'}})

# 计数
count = stuCollection.find({'age': {'$gte': 20}}).count()
print('Count：', count)

# 排序
results = stuCollection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 偏移 skip(2)从第三个开始 limit(2) 然后取两个结果
results = stuCollection.find().sort('name', pymongo.DESCENDING).skip(2).limit(2)

results = stuCollection.find({'_id': {'$gt': '5b582447c7cf384e90ae1495'}})

# 更新
condition = {'name': 'hanxiaocu'}
student = stuCollection.find_one(condition)
student['age'] = 100
result = stuCollection.update_one(condition, {'$set': student})
print(result)


condition = {'age': {'$gt': 20}}
# 年龄加1
result = stuCollection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

# 删除
result = stuCollection.delete_one({'name': 'hanxiaocu'})
print(result)
result = stuCollection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)

# 其他操作
