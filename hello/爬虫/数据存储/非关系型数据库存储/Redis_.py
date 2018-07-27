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
# 正则匹配
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
redis.lrem('list', 2, 3)
# 返回并且删除的首元素
redis.lpop('list')
# 返回并且删除的尾元素
redis.rpop('list')
# 批量删除首元素 如果列表为空,将会阻塞，timetou=0一直等待
redis.blpop('list', 'list2', timeout=0)
redis.rlpop('list', 'list2', timeout=0)
# 返回并删除名称为src的列表的尾元素，并将该元素添加到名称为dst的列表头部
redis.rpoplpush('list', 'list2')

"""集合操作 集合中的数据都是不重复的"""
# 向集合中添加数据
redis.sadd('tags', 'Book', 'Tea', 'Coffee')
# 从键为name的集合中删除元素
redis.srem('tags', 'Coffee')
# 随机返回并删除键为name的集合中的一个元素
redis.spop('tags')
# 从src对应的集合中移除元素并将其添加到dst对应的集合中
redis.smove('tags', 'tags2', 'Coffee')
# 返回键为name的集合的元素个数
redis.scard('tags')
# 测试member是否是键为name的集合的元素
redis.sismember('tags', 'Book')
# 返回所有给定键的集合的交集
redis.sinter(['tags', 'tags2'])
# 求交集并将交集保存到dest的集合
redis.sinterstore('intertag', ['tags', 'tags2'])
# 返回所有给定键的集合的并集
redis.sunion(['tags', 'tags2'])
# 求并集并将并集保存到dest的集合
redis.sunionstore('uniontag', ['tags', 'tags2'])
# 返回所有给定键的集合的差集
redis.sdiff(['tags', 'tags2'])
# 求差集并将差集保存到dest集合
redis.sdiffstore('difftag', ['tags', 'tags2'])
# 返回键为name的集合的所有元素
redis.smembers('tags')
# 随机返回键为name的集合中的一个元素，但不删除元素
redis.srandmember('tags')

"""有序集合操作 比集合多了一个分数字段score，利用它可以对集合中的数据进行排序"""
# 向集合中添加元素
redis.zadd('grade', 100, 'Bob', 98, 'mick')
# 删除键为name的元素
redis.zrem('grade', 'Mike')
# 查找对应的元素 -2 ，如果不存在 则插入 score 为-2
redis.zincrby('grade', 'Bob', -2)
# score从小到大排序 得到Amy的倒数排名
redis.zrank('grade', 'Amy')
# 返回键为name的zset（按score从大到小排序）中index从start到end的所有元素 返回键为grade的zset中前四名元素
redis.zrevrange('grade', 0, 3)
# 返回score在这个范围的所有元素
redis.zrangebyscore('grade', 80, 95)
# 同上返回个数
redis.zcount('grade', 80, 95)
# 返回集合中元素个数
redis.zcard('grade')
# 删除 排名在给定区间的元素 下面这个意思是删除第一个元素0-0
redis.zremrangebyrank('grade', 0, 0)
# 同上 删除score在此区间的元素
redis.zremrangebyscore('grade', 80, 90)


""" 散列操作 """
# 添加映射
redis.hset('price', 'cake', 5)
# 不存在再添加
redis.hsetnx('price', 'book', 6)
# 取值
redis.hget('price', 'cake')
# 返回键列表中的对应值
redis.hmget('price', ['apple', 'orange'])
# 批量添加映射
redis.hmset('price', {'banana': 2, 'pear': 6})
# 将键为name的散列表中映射的值增加amount
redis.hincrby('price', 'apple', 3)
# 判断是否存在
redis.hexists('price', 'banana')
# 删除
redis.hdel('price','banana')
# 返回个数
redis.hlen('price')
# 取所有的键名
redis.hkeys('price')
# 所有的键值
redis.hvals('price')
# 获取所有的键值对
redis.hgetall('price')

""" RedisDump提供了强大的Redis数据的导入和导出功能 """
'''
redis-dump -h 查看对应命令
-u代表Redis连接字符串，
-d代表数据库代号，
-s代表导出之后的休眠时间，
-c代表分块大小，默认是10000，
-f代表导出时的过滤器，
-O代表禁用运行时优化，
-V用于显示版本，
-D表示开启调试

只导出1号数据库 以adsl开头的数据 导出为json文件
redisr -dump -u :foobared@localhost:6379 -d 1 -f adsl:* > ./redis.data.jl 
每条数据都包含6个字段，
其中db即数据库代号，key即键名，ttl即该键值对的有效时间，type即键值类型，value即内容，size即占用空间


redis-load -h 查看对应命令
-u代表Redis连接字符串，
-d代表数据库代号，默认是全部，
-s代表导出之后的休眠时间，
-n代表不检测UTF-8编码，
-V表示显示版本，
-D表示开启调试

将json 文件导入数据库
< redis.data.json redis-load -u :foobared@localhost:6379



'''

