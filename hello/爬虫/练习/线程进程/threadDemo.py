# coding: utf-8


# 在Python中多线程不是并行是并发，一个进程只有一个GIL  全局解释器锁，所以多进程才是Python 并行的选择方式，只针对多核CPU

import time, _thread

import threading


# # 为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % threadName, time.ctime(time.time()))

# 
# try:
#     _thread.start_new_thread(print_time, ("thread1", 2))
#     _thread.start_new_thread(print_time, ('thread2', 4))
# except:
#     print('Error： 创建线程失败')
# 
# 
# while 1:
#     pass
# 
# print('main finished')


exitFlag = 0
threadLock = threading.Lock()
threads = []
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.counter = counter
        self.name = name
        self.threadID = threadID
    def run(self):
        print('starting ' + self.name)
        '''
        同步阻塞
        '''
        # 获得锁 如果成功返回true timeout 不填将一直阻塞直到获得锁，超时返回false
        threadLock.acquire()
        print_time(self.name,self.counter,5)
        # 释放锁
        threadLock.release()
        print('Exiting ' + self.name)




def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            _thread.exit()
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThread(1,'thread1',1)
thread2 = myThread(2,'thread2',2)

thread1.start()
thread2.start()

# 线程池
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print('exiting main thread')





















