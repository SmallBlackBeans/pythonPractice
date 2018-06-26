# coding: utf-8


import urllib
from urllib import request
import re
import _thread
import time


# 糗事百科
class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {
            'User-Agent': self.user_agent,
        }
        # 存储段子
        self.stories = []
        self.enable = False

    def getPageData(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            pageData = response.read().decode('utf-8')
            return pageData
        except urllib.request.URLError as e:
            if hasattr(e, 'reason'):
                print('获取数据失败，原因:' % e.reason)
                return None

    # 传入某一夜的数据，进行解析
    def getPathItems(self, pageIndex):
        pageData = self.getPageData(pageIndex)
        if not pageData:
            print('页面加载失败')
            return None
        pattern = re.compile('<div.*?author clearfix">.*?<a.*?<a.*?<h2>(.*?(?#用户姓名))</h2>.*?<span>(.*?(?#内容))</span>',
                             re.S)
        # re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。
        items = re.findall(pattern, pageData)
        # 本页面的段子集合
        pagestories = []
        for item in items:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, "\n", item[1])
            pagestories.append([item[0].strip(), text.strip()])
        return pagestories

    # 加载数据 并且显示在列表中
    def loadPage(self):
        if self.enable:
            if len(self.stories) < 2:
                # 获取新的一页
                pageStories = self.getPathItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    # 查看一个段子
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            in_put = input()
            self.loadPage()
            if in_put == 'Q':
                self.enable = False
                return
            print(u'第%ld页\n发布人：%s\n发布内容：\n%s\n' % (page, story[0], story[1]))

    def start(self):
        print(u'正在读取糗事百科，按回车查看段子，Q退出')
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)


spider = QSBK()
spider.start()
