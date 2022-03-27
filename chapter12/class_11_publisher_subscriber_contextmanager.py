# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_11_publisher_subscriber_contextmanager.py
# Time       ：2022/3/27 22:32
# Author     ：Zhong Lei
"""
from collections import defaultdict
from abc import abstractmethod
from contextlib import contextmanager


class Task:
    @abstractmethod
    def send(self):
        pass


class Display(Task):
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {}'.format(self.count, msg))


class SendMessage:
    def send(self, msg):
        print('sending {}'.format(msg))


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task: Task):
        self._subscribers.add(task)

    def detach(self, task: Task):
        self._subscribers.remove(task)

    def send(self, msg):
        for sub in self._subscribers:
            sub.send(msg)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

_exchanges = defaultdict(Exchange)

def get_exchanges(name):
    return _exchanges[name]


if __name__ == '__main__':
     t1 = Display()
     t2 = SendMessage()
     exc = get_exchanges('name')
     with exc.subscribe(t1, t2):
         exc.send('a')
