from redis import StrictRedis, ConnectionPool, Connection

redis = StrictRedis(host='localhost', port=6379, db=0, password='foobared')
# 或者
conn = Connection(host='localhost', port=6379, db=0, password='foobared')
pool = ConnectionPool(conn)
redis = StrictRedis(connection_pool=pool)
# 或则
'''
redis://[:password]@host:port/db
rediss://[:password]@host:port/db
unix://[:password]@/path/to/socket.sock?db=db
'''
url = 'redis://:foobared@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)

redis.set('name', 'Bob')
print(redis.get('name'))

"""键操作"""
# 判断是否存在
redis.exists('name')
# 删除
# redis.delete('name')
# 获取键的类型
redis.type('name')
# 匹配
redis.keys('n*')
# 随机一个键
redis.randomkey()
# 重命名
redis.rename('name', 'nickname')
# 获取键的数目
redis.dbsize()
# 设置键的过期时间 2秒
redis.expire('name', 2)
# 获取键的过期时间 -1表示永远不过期
redis.ttl('name')
# 将键移动到其他数据库 移动到2号数据库
redis.move('name', 2)
# 删除当前选择数据库中所有的键
redis.flushdb()
# 删除所有数据库中的所有键
redis.flushall()

"""字符串操作"""
# 设值
redis.set('age', 20)
# 取值
redis.get('age')
# 设置新值 返回旧值
redis.getset('name', 'newValue')
# 返回多个键对应的值
redis.mget(['name', 'nikename'])
# 如果不存在这个键值对 则更新value 否则不变
redis.setnx('newname', 'heihei')
# 设值饼设值有效期
redis.setex('name', 1, 'James')
# 设值指定键的value 的子字符串
redis.set('name', 'Hello')
redis.setrange('name', 6, 'World')
# 批量赋值
redis.mset({'name1': 'Smith', 'name2': 'Curry'})
# 键都不存在时才批量赋值
redis.msetnx({'name3': 'Smith', 'name4': 'Curry'})
# 增操作
redis.incr('age', 1)
# 减操作 不存在 则设置为-1
redis.decr('age', 1)
# 追加 返回长度
redis.append('name', 'OK')
# 截取子串 默认截取到末尾
redis.substr('name', 1, end=-1)
redis.getrange('name', 1, 4)

"""列表操作"""
# name-list 尾部添加
redis.rpush('list', 1, 2, 3)
# name-list 头部添加
redis.lpush('list', 0)
# 返回长度 以上三个都是返回列表大小
redis.llen('list')
# 取范围 返回列表
redis.lrange('list', 1, 3)
# 截取，保留范围内容 返回bool
redis.ltrim('list', 1, 3)
# 取索引元素 返回元素
redis.lindex('list', 1)
# 赋值 返回bool
redis.lset('list', 1, 5)
# 删除值为value(3)的指定个数(2)的元素 返回删除的个数
redis.lrem('list',2,3)
# 返回并且删除的首元素
redis.lpop('list')
# 返回并且删除的尾元素
redis.rpop('list')
# 批量删除首元素 如果列表为空,将会阻塞，timetou=0一直等待
redis.blpop('list','list2',timeout=0)
redis.rlpop('list','list2',timeout=0)
# 返回并删除名称为src的列表的尾元素，并将该元素添加到名称为dst的列表头部
redis.rpoplpush('list', 'list2')

"""集合操作 集合中的数据都是不重复的"""
# 向集合中添加数据
redis.sadd('tags', 'Book', 'Tea', 'Coffee')
# 从键为name的集合中删除元素
redis.srem('tags','Coffee')
# 随机返回并删除键为name的集合中的一个元素
redis.spop('tags')
# 从src对应的集合中移除元素并将其添加到dst对应的集合中
redis.smove('tags', 'tags2', 'Coffee')
# 返回键为name的集合的元素个数
redis.scard('tags')
# 测试member是否是键为name的集合的元素
redis.sismember('tags','Book')
# 返回所有给定键的集合的交集
redis.sinter(['tags','tags2'])
# 求交集并将交集保存到dest的集合
redis.sinterstore('intertag', ['tags', 'tags2'])
# 返回所有给定键的集合的并集
redis.sunion(['tags','tags2'])
# 求并集并将并集保存到dest的集合
redis.sunionstore('uniontag', ['tags', 'tags2'])
# 返回所有给定键的集合的差集
redis.sdiff(['tags','tags2'])
# 求差集并将差集保存到dest集合
redis.sdiffstore('difftag', ['tags', 'tags2'])
# 返回键为name的集合的所有元素
redis.smembers('tags')
# 随机返回键为name的集合中的一个元素，但不删除元素
redis.srandmember('tags')

"""有序集合操作 比集合多了一个分数字段，利用它可以对集合中的数据进行排序"""
