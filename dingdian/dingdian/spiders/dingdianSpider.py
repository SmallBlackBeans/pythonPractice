# coding: utf-8
import scrapy
import re
import lxml
from bs4 import BeautifulSoup
from dingdian.items import DingdianItem, DcontentItem
from scrapy.http import Request


class MySpider(scrapy.Spider):
    name = 'dingdian' # 在 entrypoint 文件中第三个参数
    allow_domains = ['23wx.com']
    base_url = 'http://www.x23us.com/class/'
    url_ext = '.html'

    def start_requests(self):
        for i in range(1, 11):  # 不包括11
            url = self.base_url + str(i) + '_1' + self.url_ext
            yield Request(url, self.parse)
        yield Request('http://www.x23us.com/quanben/1', self.parse)

    def parse(self, response):
        pattern = re.compile('<div class="pagelink.*?class="last">(.*?)</a>')
        max_num = re.findall(pattern,response.text)[0]
        # max_num = page_div.find_all('a')[-1].get_text()
        baseUrl = str(response.url)[:-7]  # 到倒数第七个
        for num in range(1, int(max_num) + 1):
            url = baseUrl + '_' + str(num) + self.url_ext
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        trs = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for tr in trs:
            alinks = tr.find('td',class_="L").find_all('a')
            if len(alinks) >= 2:
                novelname = alinks[1].get_text()
                novelUrl = alinks[1]['href']
                if str(r"http://www.x23us.com") in novelUrl:
                    print(novelname,novelUrl)
                    yield Request(novelUrl, callback=self.get_chapterurl, meta={'name': novelname,
                                                                        'url': novelUrl})

    def get_chapterurl(self, response):
        item = DingdianItem()
        item['name'] = str(response.meta['name']).replace('\xa0', '')
        item['novelurl'] = response.meta['url']
        soup = BeautifulSoup(response.text, 'lxml')
        category = soup.find('table').find('a').get_text()
        author = soup.find('table').find_all('td')[1].get_text()
        base_url = soup.find('p', class_='btnlinks').find('a', class_='read')['href']
        name_id = str(base_url)[-6:-1].replace('/', '')
        item['category'] = str(category).replace('/', '')
        item['author'] = str(author).replace('/', '')
        item['name_id'] = str(name_id).replace('/', '')
        yield item # 这个返回的是一个item的生成器,可以是用next(函数) 进行遍历
        # 剩下的貌似要登录，哥哥不搞了
        #yield Request(url=base_url, callback=self.get_chapter, meta={'name_id': name_id})

    # def get_chapter(self, response):
    #     com = re.compile(r'<td class="L"><a href="(.*?)">(.*?)</a></td>')
    #     urls = re.findall(com, response.text)
    #     num = 0  # 做排序
    #     for url in urls:
    #         num = num + 1
    #         chapter_url = response.url + url[0]
    #         chapter_name = url[1]
    #         rets = Sql.select_chapter(chapter_url)
    #         if rets[0] == 1:
    #             print('章节已经存在了')
    #             pass
    #         else:# 做判断减少了网络请求
    #             yield Request(chapter_url, callback=self.get_chapterContent,
    #                           meta={
    #                               'num': num,
    #                               'name_id': response.meta['name_id'],
    #                               'chaptername': chapter_name,
    #                               'chapterurl': chapter_url
    #                           })
    #
    # def get_chapterContent(self, response):
    #     item = DcontentItem()
    #     item['num'] = response.meta['num']
    #     item['id_name'] = response.meta['name_id']
    #     item['chaptername'] = str(response.meta['chaptername']).replace('\xa0', '')
    #     item['chapterurl'] = str(response.meta['chapterurl']).replace('\xa0', '')
    #     content = BeautifulSoup(response.text, 'lxml').find('dd', id='contents').get_text()
    #     item['chaptercontent'] = str(content).replace('\xa0', '')
    #     return item
