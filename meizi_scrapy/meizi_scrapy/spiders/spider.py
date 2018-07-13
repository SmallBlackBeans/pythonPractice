from scrapy import Request,http
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from meizi_scrapy.items import MeiziScrapyItem


class Spider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com','i.meizitu.net']
    start_urls = ['http://www.mzitu.com/']
    img_urls = []
    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',), deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response:http.Response):
        item = MeiziScrapyItem()
        # descendant 选取当前节点的所有后代元素（子、孙等)
        max_num = response.xpath(
            "descendant::div[@class='main']/div[@class='content']/div[@class='pagenavi']/a[last()-1]/span/text()").extract_first(
            default="N/A")
        item['name'] = response.xpath("./*//div[@class='main']/div[1]/h2/text()").extract_first(default="N/A")
        item['url'] = response.url
        print(response.url)
        # yield 是一个生成器 下面这个for 循环 将是一个整体，返回 所有 self.img_url 的结果情况，可以理解为占位，即使是网络请求，个人理解 哈哈
        for num in range(1,int(max_num)):
            page_url = response.url + '/' + str(num)
            yield Request(page_url,callback=self.img_url)
        item['image_urls'] = self.img_urls
        yield item

    def img_url(self,response):
        # descendant::div[@class=’main-image’]/descendant::img/@src这段xpath取出div[@class=’main-image’]下面所有的img标签的src属性
        img_urls = response.xpath("descendant::div[@class='main-image']/descendant::img/@src").extract()
        for img_url in img_urls:
            self.img_urls.append(img_url)