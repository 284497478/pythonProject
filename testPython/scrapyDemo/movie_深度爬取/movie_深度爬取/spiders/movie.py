import scrapy
from movie_深度爬取.items import MovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.k8jds.com/index.php/vod/show/id/5.html']
    url = 'https://www.k8jds.com/index.php/vod/show/id/5/page/%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[2]/div/div[2]/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div/a/@title').extract_first()
            detail_url = 'https://www.k8jds.com/' + li.xpath('./div/a/@href').extract_first()
            item = MovieItem()
            item['title'] = title

            yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'item': item})
        if self.page_num < 5:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

    def detail_parse(self, response):
        detail = response.xpath('/html/body/div[2]/div/div[1]/div[4]/div/div[2]/div/span[1]').extract_first()
        item = response.meta['item']
        item['detail'] = detail
        yield item
