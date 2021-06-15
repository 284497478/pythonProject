'''

    针对代码：1.协程基础、
            2.asyncio单线程-多任务操作
            3.单线程-多任务例子

    特殊函数：
        如果一个函数的定义被async修饰后，则改函数变成一个特殊函数
        特殊之处：
            该特殊的函数条用后，函数内部的实现语句不会被立即执行
            该特殊函数被调用后，返回一个协程对象
    协程对象：
        对象。通过特殊函数的调用返回一个协程对象
        协程 ==》特殊函数 ==》一组指定的操作，通常为定义为async的函数
    任务对象
        任务对象就是一个高的协程对象。（任务对象就是对协程对象的进一步封装）
        任务 == 协程 == 特殊函数 == 一组指定的操作
        任务 == 一组指定的操作
        如何创建一个任务对象
            asyncio.ensure_future(c)
        任务对象的高级之处
            可以给任务对象绑定回调：
                task.add_done_callback(task_callback)
                回调函数的调用时机：
                    任务被执行结束后才可以调用回调函数
                回调函数的参数只可以有一个：表示的就是该回调函数的调用者（其实就是任务对象）
                使用回调函数的参数调用result（）返回的就是任务对象表示的特殊函数return的结果
    事件循环对象
        对象
        作用：
            可以将多个任务对象注册/装载到事件循环对象中。
            如果开启了时间循环后，则其内部注册/装载的任务对象表示的指定操作就会被基于异步的被执行
        创建方式：
            loop = asyncio.get_event_loop()
        注册且启动方式：
            loop.run_until_complete(task)
    wait 方法的作用：
        将任务列表中的任务对象赋予可被挂起的权限，只有任务对象被赋予了可被挂起的权限后，该任务对象才可以被挂起
            挂起：将当前的任务对象交出cpu的使用权
    注意事项
        在特殊函数内部不可以出现不支持异步模块对应的代码，否则会中断整个异步效果。

    await关键字
        在特殊函数内部，凡是阻塞操作前都必须使用await进行修饰，await就可以保证阻塞操作在异步执行过程中不会被跳过。


    使用多任务的异步协程爬取数据实现套路：
        可以先用request模块将带请求的数据对应的url封装到一个列表中，如将资源的src保存到列表中（同步操作）
        在使用aiohttp模式将列表的url进行异步请求和数据解析（异步操作）
'''

import asyncio
import requests
import time


async def get_request(url):
    print('正在请求url:', url)
    time.sleep(2)
    print('请求结束：', url)
    return 'get_request(),return结果'


# 回调函数封装
# 参数str：就是该回调函数的调用者（任务对象）
def task_callback(str):
    print('我是task_callback(),参数str：', str)
    print('str.result()返回的是：', str.result())


if __name__ == "__main__":
    # 对async标识的函数进行执行，返回一个协程对象c
    c = get_request("www.baidu.com")
    # 任务对象就是对协程对象的进一步封装，得到task就是任务对象
    task = asyncio.ensure_future(c)
    # 给task绑定一个回调函数
    task.add_done_callback(task_callback)
    # 创建一个事件循环对象
    loop = asyncio.get_event_loop()
    # 将任务对象注册到事件循环对象
    loop.run_until_complete(task)
    # print(c)
