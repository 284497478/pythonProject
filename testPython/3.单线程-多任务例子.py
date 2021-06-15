import asyncio
import time
from lxml import etree

import aiohttp
import requests

urls = [
    "http://127.0.0.1:5000/test1",
    "http://127.0.0.1:5000/test2",
    "http://127.0.0.1:5000/test3"
]


# 异步操作不可以用requests模块，因为是不支持异步的模块
# 需要换成aiohttp
# async def get_request(url):
#     page_text = requests.get(url).text
#     return page_text


# 需要注意的是由于要异步操作
# 每个with 前面都需要加入async标识
# 并且每个阻塞操作需要加入await标识
async def get_request(url):
    # 实例化一个aiohttp请求对象
    async with aiohttp.ClientSession() as sess:
        # 调用get发起一个请求，返回一个请求对象
        async with await sess.get(url) as resp:
            # text()获取字符串形式的响应数据
            # read()获取byte类型的响应数据
            page_text = await resp.text()
            return page_text


# 解析函数
def convert_data(t):
    page_text = t.result()
    tree = etree.HTML(page_text)
    data = tree.xpath('//body/text()')[0]
    print(data)


if __name__ == "__main__":
    start = time.time()
    tasks = []
    for url in urls:
        # 1.创建协程对象
        c = get_request(url)
        # 2.创建任务对象
        task = asyncio.ensure_future(c)
        task.add_done_callback(convert_data)
        tasks.append(task)
    # 3.创建时间循环对象
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('ts :', time.time() - start)
