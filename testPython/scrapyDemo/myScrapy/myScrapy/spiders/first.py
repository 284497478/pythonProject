import scrapy

'''
    一、scrapy的基本使用
        1.创建scrapy工程
            scrapy startproject ProName
            目录：
                spiders：爬虫文件夹
                必须存放一个爬虫源文件
            settings.py 工程的配置文件
    二、cd ProName
    三、创建爬虫源文件：
        scrapy genspide spiderName www.***.com
    四、执行工程
        scrapy crawl spiderName
'''


class FirstSpider(scrapy.Spider):
    #爬虫文件名
    name = 'first'
    # 允许执行的url地址，如果打开，start_urls中的url只会执行与其对应的网址，一般关掉
    # allowed_domains = ['www.xxx.com']
    #自动爬取的网站，都会发送get请求
    start_urls = ['https://www.baidu.com/', 'https://www.jd.com']

    def parse(self, response):
        print('resp', response)
