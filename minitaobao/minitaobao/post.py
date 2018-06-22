# coding: utf-8

from django.views.decorators import csrf
from django.shortcuts import render


def search_post(request):
    ctx = {}
    if request.method == "POST":
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
