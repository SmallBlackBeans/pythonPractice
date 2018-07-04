from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from scrapy import FormRequest

from dingdian.items import HaodufuliItem

account = ''
password = ''


class myCrawSpider(CrawlSpider):
    name = 'haodufuli'
    allowed_domains = ['haoduofuli.wang']
    start_urls = ['www.haoduofuli.wang/login.php']

    def parse_start_url(self, response):
        formdata = {
            'log': account,
            'pwd': password,
            'rememberme': 'forever',
            'wp_submit': '登录',
            'redirect_to': 'http://www.haoduofuli.wang/wp-admin/',
            'testcookie': "1"
        }
        return [FormRequest.from_response(response, formdata=formdata, callback=self.after_login)]

    def after_login(self, response):
        link = 'http://www.haoduofuli.wang'
        return Request(link)

    rules = (
        Rule(LinkExtractor(allow=('\.html',)), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = HaodufuliItem()
        try:
            item['category'] = response.xpath('//*[@id="content"]/div[1]/div[1]/span[2]/a/text()').extract()[0]
            item['title'] = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract()[0]
            item['imgurl'] = response.xpath('//*[@id="post_content"]/p/img/@src').extract()
            item['yunlink'] = response.xpath('//*[@id="post_content"]/blockquote/a/@href').extract()[0]
            item['password'] = response.xpath('//*[@id="post_content"]/blockquote/font/text()').extract()[0]
            return item
        except:
            item['category'] = response.xpath('//*[@id="content"]/div[1]/div[1]/span[2]/a/text()').extract()[0]
            item['title'] = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract()[0]
            item['imgurl'] = response.xpath('//*[@id="post_content"]/p/img/@src').extract()
            item['yunlink'] = response.xpath('//*[@id="post_content"]/blockquote/p/a/@href').extract()[0]
            item['password'] = response.xpath('//*[@id="post_content"]/blockquote/p/span/text()').extract()[0]
            return item


