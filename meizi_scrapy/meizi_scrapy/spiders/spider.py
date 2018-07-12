from scrapy import Request,http
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from meizi_scrapy.items import MeiziScrapyItem


class Spider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/']
    img_urls = []
    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',), deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response:http.Response):
        item = MeiziScrapyItem()
        max_num = response.xpath(
            "descendant::div[@class='main']/div[@class='content']/div[@class='pagenavi']/a[last()-1]/span/text()").extract_first(
            default="N/A")
        item['name'] = response.xpath("./*//div[@class='main']/div[1]/h2/text()").extract_first(default="N/A")
        item['url'] = response.url
        for num in range(1,int(max_num)):
            # page_url =
    