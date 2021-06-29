import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.xxxx.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
