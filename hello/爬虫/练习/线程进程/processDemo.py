# coding: utf-8


# 多进程


import multiprocessing
import time


def process(num):
    time.sleep(num)
    print('Process: ', num)


# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#
#     print('CPU number: ' + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('child process name: ' + p.name + ' pid: ' + str(p.pid))
#
#     print('process ended')

from multiprocessing import Process, Lock


class myProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.lock = lock
        self.loop = loop

    # 实现这个方法
    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            self.lock.acquire()
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
            self.lock.release()


# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(2, 5):
#         p = myProcess(i, lock)
#         p.daemon = True  # 设置为True，当父进程结束后，子进程会自动被终止 即主线程直接完了，这些子线程不会做操作
#         p.start()
#         p.join()  # 和daemon 相反，父进程会等到所有的子进程执行完毕
#
#     print('main process ended!')


'''
Semaphore 信号量
'''
from multiprocessing import Queue, Semaphore
buffer = Queue(10)  # 进程间的通信，队列需要用Queue
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()
class Consumer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()
            lock.acquire()
            buffer.get()
            print('Consumer pop an element')
            time.sleep(1)
            lock.release()
            empty.release()

class Producer(Process):
    def run(self):
        global buffer,empty,full,lock
        while True:
            empty.acquire()
            lock.acquire()
            buffer.put(1)
            print('Producer append an element')
            time.sleep(1)
            lock.release()
            full.release()

# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     p.daemon = c.daemon = True
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#     print('Ended!')



'''
Pipe 管道 一端发 一端接
'''