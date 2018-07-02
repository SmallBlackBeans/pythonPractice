# coding: utf-8
import scrapy
import re
from bs4 import BeautifulSoup
from dingdian.items import DingdianItem
from scrapy.http import Request


class MySpider(scrapy.Spider):
    name = 'dingdian'
    allow_domains = ['23wx.com']
    base_url = 'http://www.x23us.com/class/'
    url_ext = '.html'

    def start_requests(self):
        for i in range(1, 11):  # 不包括11
            url = self.base_url + str(i) + '_1' + self.url_ext
            yield Request(url, self.parse)
        yield Request('http://www.x23us.com/quanben/1', self.parse)

    def parse(self, response):
        print(response.text)
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        baseUrl = str(response.url)[:-7]  # 到倒数第七个
        for num in range(1, int(max_num) + 1):
            url = baseUrl + '_' + str(num) + self.url_ext
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        trs = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for tr in trs:
            a = tr.find('a')
            novelname = a.get_text()
            novelUrl = a['href']
            yield Request(novelUrl,callback=self.get_chapterurl,meta={'name':novelname,
                                                                      'url':novelUrl})

    def get_chapterurl(self,response):
        item = DingdianItem()
        item['name'] = str(response.meta['name']).replace('\xa0','')
        item['novelurl'] = response.meta['url']
        soup = BeautifulSoup(response.text,'lxml')
        category = soup.find('table').find('a').get_text()
        author = soup.find('table').find_all('td')[1].get_text()
        base_url = soup.find('p',class_='btnlinks').find('a',class_='read')['href']
        name_id = str(base_url)[-6:-1].replace('/','')
        item['category'] = str(category).replace('/','')
        item['author'] = str(author).replace('/','')
        item['name_id'] = str(name_id).replace('/','')
        return item
spider = MySpider()
spider.start_requests()
