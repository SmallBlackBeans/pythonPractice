# coding: utf-8


import queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter, q):
        threading.Thread.__init__(self)
        self.name = name
        self.threadId = threadId
        self.counter = counter
        self.q = q

    def run(self):
        print('starting ' + self.name)
        process_data(self.name, self.q)
        print('exiting ' + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print('%s processing %s ' % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ['thread1', 'thread2', 'thread3']
nameList = ['one', 'two', 'three', 'four', 'five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程退出
exitFlag = 1

for t in threads:
    t.join() #  实际上意味着等到队列为空，再执行别的操作

print('exiting main thread')
