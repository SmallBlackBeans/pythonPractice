# -*- coding: utf-8 -*-
# from django.http import HttpResponse
#
#
# def hello(request):
#     return HttpResponse("Hello world ! ")



# from django.http import HttpResponse
from django.shortcuts import render


# 实现数据与视图分离
def hello(request):
    context = {}#字典
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)