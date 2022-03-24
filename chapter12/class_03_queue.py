from threading import Thread
from queue import Queue
import queue
from heapq import heappush, heappop
import time

# consumer and producer
def producer(q: Queue, data):
    while True:
        try:
            q.put(data, timeout=0.5)
            time.sleep(0.03)
        except queue.Full:
            print('queue full')
    # 放入哨兵的方式记录 q.put(sential)

def consumer(q: Queue):
    while True:
        try:
            data = q.get(block=False, timeout=0.5)
            time.sleep(0.1)
            print(data)
        except queue.Empty:
            print('queue empty')


q = Queue(maxsize=10)
t1 = Thread(target=producer, args=(q, 1))
t2 = Thread(target=consumer, args=(q, ))
t3 = Thread(target=consumer, args=(q, ))
t4 = Thread(target=consumer, args=(q, ))

t1.start()
t2.start()
t3.start()
t4.start()