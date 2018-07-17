#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
from py2neo import Node, Relationship, NodeMatch,NodeMatcher
from pandas import DataFrame

a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
r = Relationship(a, 'KNOWS', b)
#
# a['age'] = 20
# b['age'] = 21
# r['time'] = '2017/08/31'
# a['location'] = '上海'
# a.setdefault('location', "北京")
#
# # 批量更新
# data = {
#     'name': 'Amy',
#     'age': 21
# }
# a.update(data)
# print(a)
# print(a, b, r)

# Subgraph 子图 是 Node 和 Relationship 的集合
s = a | b | r
print(s)
print(s.keys())
print(s.labels)
print(s.nodes)
print(s.relationships)
print(s.types())

# Walkable 可遍历的Subgraph
c = Node('Person', name='Mike')
ab = Relationship(a, "KNOWS", b)
ac = Relationship(a, "KNOWS", c)
w = ab + Relationship(b, "LIKES", c) + ac
# print(w)

# Graph
from py2neo import Graph

# 创建
graph_1 = Graph()
graph_2 = Graph(host='localhost')
graph_3 = Graph('http://localhost:7474/db/data/')
s = a | b | r
graph = Graph(password='123456')
# 添加
graph.create(s)

# 查找
data = graph.data('MATCH (p:Person) return p')
print(data)
#### DataFrame
df = DataFrame(data)

node = graph.find_one(label='Person')
print(node)
relationship = graph.match_one(rel_type='KNOWS')
print(relationship)

# 更新
node = graph.find_one(label='Person')
node['age'] = 21
graph.push(node)

# 删除  Node 时必须先删除其对应的 Relationship，否则无法删除 Node
node = graph.find_one(label='Person')
relationship = graph.match_one(rel_type='KNOWS')
graph.delete(relationship)
graph.delete(node)

# 执行CQL
data = graph.run("MATCH (p:Person) "
                 "RETURN p.name,p.age LIMIT 5")
print(list(data))
data.to_table()

'''
https://py2neo.org/v4/ogm.html?highlight=graphobject%20select#py2neo.ogm.GraphObjectMatch
'''
from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom


class Person(GraphObject):
    __primarykey__ = 'name'
    name = Property()
    born = Property()
    acted_in = RelatedTo('Movie')
    directed = RelatedTo('Movie')
    produced = RelatedTo('Movie')

class Movie(GraphObject):
    __primarykey__ = 'title'

    title = Property()
    released = Property()
    actors = RelatedFrom('Person','ACTED_IN')
    directors = RelatedFrom('Person','DIRECTED')
    productors = RelatedFrom('Person','PRODUCED')



list = [(a.name, a.born) for a in Person.match(graph).limit(3)]

graph = Graph(password='123456')
a = Node('Person', name='Alice', age=21, location='广州')
b = Node('Person', name='Bob', age=22, location='上海')
c = Node('Person', name='Mike', age=21, location='北京')
r1 = Relationship(a, 'KNOWS', b)
r2 = Relationship(b, 'KNOWS', c)
graph.create(a)
graph.create(r1)
graph.create(r2)

matcher = NodeMatcher(graph)
# 等价于
matcher = graph.nodes
persons = matcher.match("Person", age='21')
person  = persons.first()

matcher.match("Person").where("_.name =~ 'K.*").order_by("_.name").limit(3)



# OGM 查询 对象和 Node 的映射
person = Person.match(graph).where(age=21).first()
print(person.__ogm__.node)
person.age = 22
print(person.__ogm__.node)
graph.push(person)

