from queue import Queue
from threading import Thread, Condition
from heapq import heappop, heappush


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = Condition()

    def put(self, item, priority):
        heappush(self._queue, (-priority, self._count, item))
        self._count += 1
        self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heappop(self._queue)[-1]


