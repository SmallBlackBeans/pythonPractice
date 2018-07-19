# coding: utf-8

import requests
from bs4 import BeautifulSoup  ##导入bs4中的BeautifulSoup
import os

from pymongo import MongoClient
from reverseDownload import down
import datetime


class mzitu:

    def __init__(self):
        client = MongoClient()
        db = client['mongoTest']  # 数据库
        self.meizitu_collection = db['meizitu']  # 数据表
        self.title = ''  # 页面主题
        self.url = ''  # 保存的页面地址
        self.img_urls = []  # 图片地址

        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def all_url(self, url):
        html = down.get(url, 3)
        soup = BeautifulSoup(html.text, 'lxml')
        all_a = soup.find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存: ', title)
            dir_name = str(title).replace('?', '_').strip()
            self.mkdir(dir_name)
            href = a['href']
            self.url = href
            if self.meizitu_collection.find_one({'主题页面':href}):
                print(u'这个页面已经爬取过了')
            else:
                self.html(href)

    def html(self, href):  ##这个函数是处理套图地址获得图片的页面地址
        html = down.get(href, 3)
        self.headers['referer'] = href
        # 获取页码
        element = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi')
        if element != None:
            max_span = element.find_all('span')[-2].get_text()
            page_num = 0 # 计数器 判断图片是否下载完毕
            for page in range(1, int(max_span) + 1):
                page_num = page_num + 1
                page_url = href + '/' + str(page)
                self.img(page_url,max_span,page_num)  ##调用img函数

    def img(self, page_url,max_span,page_num):  ##这个函数处理图片页面地址获得图片的实际地址
        img_html = down.get(page_url, 3)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.img_urls.append(img_url)
        if int(max_span) == page_num:
            self.save(img_url)
            post = {
                '标题':self.title,
                '主题页面':self.url,
                '图片地址':self.img_urls,
                '获取时间':datetime.datetime.now()
            }
            self.meizitu_collection.save(post)
            print(u'插入数据库成功')
        else:
            self.save(img_url)

    def save(self, img_url):  ##这个函数保存图片
        name = img_url[-9:-4]
        img = down.get(img_url, 3)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("/Users/hanchenghai/Desktop/meizi/", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("/Users/hanchenghai/Desktop/meizi", path))
            os.chdir(os.path.join("/Users/hanchenghai/Desktop/meizi", path))  ##切换到目录
            return True
        else:
            # print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False


Mzitu = mzitu()
Mzitu.all_url('http://www.mzitu.com/all')
