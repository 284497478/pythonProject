import asyncio
import time


# 特殊函数
async def async_method(params):
    print('async_method is begin')
    print(params)
    print('async_method is endding')
    return 'async_result'


def async_callback_method(t):
    print('async_callback running')
    print('async_callback 传入参数内容：', t)
    print('async_callbakc 特殊函数的返回结果t.result() :', t.result())


if __name__ == "__main__":
    # 1.创建协程对象,
    c = async_method('test1')
    # 2.创建任务对象
    task = asyncio.ensure_future(c)
    # 2.1添加回调函数
    task.add_done_callback(async_callback_method)
    # 3.创建事件循环对象
    loop = asyncio.get_event_loop()
    # 4.装载任务对象到事件循环对象中
    loop.run_until_complete(task)
