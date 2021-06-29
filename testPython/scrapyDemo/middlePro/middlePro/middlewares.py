# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    # 拦截所有（正常&异常）请求
    # 参数 request就是拦截到的请求，spider就是爬虫实例化的对象
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # request.headers['User-Agent'] = 'xxxx'
        # request.headers['Cookie'] = 'xxxx'
        print('process_request()')
        return None  # or request

    # 拦截所有响应
    # 参数：respose拦截到的响应对象，request响应对象对应的请求对象
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

        print('process_response()')
        return response

    # 拦截异常的请求
    # 参数：request就是拦截到的发生异常的请求
    # 作用：想要讲异常的请求进行修正
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        # 请求的ip被禁用，改请求就会变成一个异常的请求
        # request.meta['proxy'] = 'http://ip:port' #设置代理
        print('process_exception')
        return request
