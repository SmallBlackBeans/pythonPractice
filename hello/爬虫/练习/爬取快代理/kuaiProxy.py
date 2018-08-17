from selenium import webdriver


class Item(object):
    ip = None
    port = None
    anonymous = None
    type = None
    local = None
    speed = None


class GetProxy(object):

    def __init__(self):
        '''
        初始化
        '''
        self.starturl = "http://www.kuaidaili.com/free/inha/"
        self.urls = self.get_urls()
        self.proxylist = self.get_porxy_list(self.urls)
        self.filename = 'proxy.txt'
        self.save_to_file(self.filename, self.proxylist)

    def get_urls(self):
        urls = []
        for i in range(1, 10)
            url = self.starturl + str(i)
            urls.append(url)
        return urls

    def get_proxy_list(self, urls):
        brower = webdriver.PhantomJS()
        proxy_list = []
        for url in urls:
            brower.get(url)
            brower.implicitly_wait(3)

            elements = brower.find_elements_by_xpath('//tbody/tr')
            for element in elements:
                item: Item = Item()
                item.ip = element.find_element_by_xpath('./td[1]').text
                item.port = element.find_element_by_xpath('./td[2]').text
                item.anonymous = element.find_element_by_xpath('./td[3]').text
                item.local = element.find_element_by_xpath('./td[4]').text
                item.speed = element.find_element_by_xpath('./td[5]').text
                proxy_list.append(item)
        brower.quit()
        return proxy_list

    def save_to_file(self, filename, proxylist):
        with open(filename,'w') as f:
            for item in proxylist:
                f.write(item.ip + '\t')
                f.write(item.port + '\t')
                f.write(item.anonymous + '\t')
                f.write(item.local + '\t')
                f.write(item.speed + '\t')


if __name__ == '__main__':
    GET = GetProxy()

