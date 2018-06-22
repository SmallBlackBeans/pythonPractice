"""minitaobao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from minitaobao import view, testdb, search, post

"""
url()
regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。
view: 用于执行与正则表达式匹配的 URL 请求。
kwargs: 视图使用的字典类型的参数。
name: 用来反向获取 URL。
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello$', view.hello),
    url(r'^db/insertData$', testdb.insertData),
    url(r'^db/findData$', testdb.findData),
    url(r'^db/updateData$', testdb.updateData),
    url(r'^db/deleteData$', testdb.deleteData),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', post.search_post),
]
