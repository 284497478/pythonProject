import scrapy


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.xxx.co']
    start_urls = ['https://www.duanziwang.com/wenzi/']
    # start_urls = ['http://www.gztxcw.com/News/newslist10_1.html']

    def parse(self, response):
        dl_list = response.xpath('/html/body/div[4]/div[1]/div[1]/dl')
        for dl in dl_list:
            title = dl.xpath('./span/dd/a/strong/text()').extract()
            content = dl.xpath('./dd/text()').extract()
            print(title, content)
            break

        # div_list = response.xpath('//*[@id="content"]/div/div/div')
        # for dl in div_list:
        #     title = dl.xpath('./div[2]/a/h4/text()').extract_first()
        #     content = dl.xpath('./div[2]/p/text()').extract_first()
        #     print(title, content)
        #     break
