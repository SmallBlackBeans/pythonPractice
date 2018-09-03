import asyncio

from asyncio import Task


async def execute(x):
    print('Number:', x)
    return x


"""定义协程"""
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
# 
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('Task: ', task)
# loop.run_until_complete(task)
# print('Task: ', task)
# print('After calling loop')
# 
# task = asyncio.ensure_future(coroutine)
# print('Task: ', task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task: ', task)
# print('After calling loop')

"""绑定回调"""
import requests


async def request():
    url = 'http://www.baidu.com'
    status = requests.get(url=url)
    return status


def callback(task):
    print('status: ', task.result())


#
# coroutine = request()
#
# task: asyncio.Task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# print('Task: ', task)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task: ', task)


""" 多任务协程"""
# tasks = [asyncio.ensure_future(request()) for _ in range(5)]
# print('Tasks:', tasks)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# for task in tasks:
#     print('Task Result: ', task.result())

"""协程实现"""
import time
import aiohttp # 异步请求操作
# 将requests.get 即 response对象包装成协程对象
async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url=url)
    result = await response.text()
    session.close()
    return result

async def mock_request():
    url = 'http://127.0.0.1:5000/'
    print('Waiting for ', url)
    result = await get(url=url) # 挂起请求 造成IO阻塞
    print('Get response from ', url, 'Rusult: ', result)

def coroutine_imp():
    start = time.time()
    tasks = [asyncio.ensure_future(mock_request()) for _ in range(5)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print('Cost time: ', end - start)



if __name__ == '__main__':
    coroutine_imp()