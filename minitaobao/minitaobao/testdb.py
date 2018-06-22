# coding: utf-8

from django.http import HttpResponse
from Model.models import Test
import string
import random


# 数据库操作
def random_string(size=13, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def insertData(request):
    test1 = Test(name=random_string())
    test1.save()
    return HttpResponse("<p>添加数据成功</p>")


def findData(request):
    response = ""
    response1 = ""

    # 相当于where
    list = Test.objects.all()

    response2 = Test.objects.filter(id=1)

    response3 = Test.objects.get(id=1)

    # 可以用来做分页 limit 10
    Test.objects.order_by('name')[0:10]

    # 排序
    Test.objects.order_by('id')

    Test.objects.filter(name='hanxiaocu').order_by('id')

    for var in list:
        response1 += var.name + ' '
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def updateData(request):
    # data = Test.objects.get(id=1)
    # data.name = '韩小醋'
    # data.save()
    Test.objects.filter(id=1).update(name='韩小醋')
    # Test.objects.all().update(//////)
    return HttpResponse("<p>修改成功</p>")


def deleteData(request):
    data = Test.objects.get(id=4)
    data.delete()

    # Test.objects.filter(id=1).delete()
    return HttpResponse("<p>删除成功</p>")