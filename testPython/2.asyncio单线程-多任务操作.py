import asyncio
import requests
import time


async def get_request(url):
    print('正在请求url:', url)
    #此处不可以用不支持异步模块的代码。否则报错，
    # 如不可使用time.sleep(),需要改成支持异步操作的代码如asyncio.sleep()
    await asyncio.sleep(2)
    print('请求结束：', url)
    return 'get_request(),return结果'


urls = [
    'www.test1.com',
    'www.test2.com',
    'www.test3.com'
]

if __name__ == "__main__":
    start = time.time()
    tasks = []
    # 1.创建协程对象
    for url in urls:
        c = get_request(url)
        # 2.创建任务对象
        task = asyncio.ensure_future(c)
        tasks.append(task)
    # 3.创建事件循环对象
    loop = asyncio.get_event_loop()
    # 单任务时可直接将任务对象放到事件循环对象中，多个任务时不行
    # loop.run_until_complete(tasks)
    # 必须使用wait方法对tasks进行封装
    loop.run_until_complete(asyncio.wait(tasks))
    #
    print("ts:", time.time() - start)
