import scrapy
from duanzishou.items import DuanzishouItem


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.xxx.co']
    start_urls = ['https://www.duanziwang.com/wenzi/']

    # start_urls = ['http://www.gztxcw.com/News/newslist10_1.html']

    # 基于终端进行持久化
    # def parse(self, response):
    #     dl_list = response.xpath('/html/body/div[4]/div[1]/div[1]/dl')
    #     all_data = []
    #     for dl in dl_list:
    #         title = dl.xpath('./span/dd/a/strong/text()').extract()
    #         content = dl.xpath('./dd/text()').extract()
    #         dic = {
    #             "title": title,
    #             "content": content
    #         }
    #         all_data.append(dic)
    #     return all_data
    # div_list = response.xpath('//*[@id="content"]/div/div/div')
    # for dl in div_list:
    #     title = dl.xpath('./div[2]/a/h4/text()').extract_first()
    #     content = dl.xpath('./div[2]/p/text()').extract_first()
    #     print(title, content)
    #     break
    '''
     基于管道
    1.在爬虫文件中进行数据解析
    2.在items.py中定义相关属性
      需要几个属性就定义几个
    3.在爬虫文件中将解析到的数据存储封装到item类型的对象中
    4.将item类型的对象提交给管道 =>yield
    5.在管道文件中（pipelines.py）中，接收爬虫文件提交过来的item类型对象，
        并且对其进行任意形式的持久化存储操作
    6.在配置文件中开启管道机制
        ITEM_PIPELINES
    '''

    def parse(self, response):
        dl_list = response.xpath('/html/body/div[4]/div[1]/div[1]/dl')
        all_data = []
        for dl in dl_list:
            title = dl.xpath('./span/dd/a/strong/text()').extract_first()
            content = dl.xpath('./dd/text()').extract_first()
            item = DuanzishouItem()
            item['title'] = title
            item['content'] = content
            # 提交给管道
            yield item
