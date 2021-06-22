# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from redis import Redis


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
        # 多个管道类的话，必选要return item
        return item


# 将数据存储到mysql

# class MysqlPileline(object):
#     conn = None
#     cursor = None
#
#     def open_spider(self, spider):
#         self.conn = pymysql.Connect(host='127.0.0.1', port=3306, db='spider', user='root', password='123456')
#         print(self.conn)
#
#     def process_item(self, item, spider):
#         self.cursor = self.conn.cursor()
#         sql = 'insert into duanziwang values ("%s","%d")' % (item['title'], item['content'],)
#
#         # 事务处理
#         try:
#             self.cursor.execute(sql)
#             self.conn.commit()
#         except Exception as e:
#             self.cursor.close()
#             self.conn.close()


# 数据写入redis
class RedisPileline(object):
    conn = None

    def open_spider(self, spider):
        self.conn = Redis(host='127.0.0.1', port=6379)
        print(self.conn)

    def process_item(self, item, spider):
        # 报错，将redis模块的版本指定成2.10.6即可 pip install -U redis==2.10.6
        item_title = str(item['title'])
        print(item_title)
        self.conn.set('duanziData', item_title)
        print(str(self.conn.get('duanziData')))
        # self.conn.lpush('duanziData', item_title)
