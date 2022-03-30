# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_12_yield_from.py
# Time       ：2022/3/28 21:32
# Author     ：Zhong Lei
"""
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
    print('Blastoff!')


def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1


from collections import deque
class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass

if __name__ == '__main__':
    t = TaskScheduler()
    t.new_task(countdown(10))
    t.new_task(countdown(5))
    t.new_task(countup(15))
    t.run()


