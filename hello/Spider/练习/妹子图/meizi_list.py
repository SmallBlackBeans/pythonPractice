# coding: utf-8

import requests
from bs4 import BeautifulSoup  ##导入bs4中的BeautifulSoup
import os


class mzitu:

    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def all_url(self, url):
        html = self.request(url)
        soup = BeautifulSoup(html.text, 'lxml')
        all_a = soup.find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存: ', title)
            dir_name = str(title).replace('?', '_').strip()
            self.mkdir(dir_name)
            href = a['href']
            self.html(href)

    def html(self,href):  ##这个函数是处理套图地址获得图片的页面地址
        html = self.request(href)
        self.headers['referer'] = href
        # 获取页码
        element = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi')
        if element != None:
            max_span = element.find_all('span')[-2].get_text()
            for page in range(1, int(max_span) + 1):
                page_url = href + '/' + str(page)
                self.img(page_url)  ##调用img函数

    def img(self, page_url):  ##这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self,img_url):  ##这个函数保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def request(self,url):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("/Users/hanchenghai/Desktop/meizi/", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("/Users/hanchenghai/Desktop/meizi", path))
            os.chdir(os.path.join("/Users/hanchenghai/Desktop/meizi", path))  ##切换到目录
            return True
        else:
            #print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False


Mzitu = mzitu()
Mzitu.all_url('http://www.mzitu.com/all')
