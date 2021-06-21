# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DuanzishouPipeline(object):
    fp = None

    # 重写父类方法
    def open_spider(self, spider):
        print('我是open_spider(),开始时候我执行')
        self.fp = open('duanzi.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        print('close_spider')
        self.fp.close()

    # 该方法接收item对象,一次只能接收一个，该方法会调用多次
    def process_item(self, item, spider):
        self.fp.write(item['title'] + ':' + item['content'] + '\n')
        return item
