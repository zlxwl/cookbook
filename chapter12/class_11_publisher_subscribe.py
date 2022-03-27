# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_11_publisher_subscribe.py
# Time       ：2022/3/27 21:32
# Author     ：Zhong Lei
"""
from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscribe in self._subscribers:
            subscribe.send(msg)

_exchanges = defaultdict(Exchange)

def get_exchange(name):
    return _exchanges[name]


class Task:
    def send(self, msg):
        print('sending ', msg)


t1 = Task()
t2 = Task()

exc = get_exchange('name')
exc.attach(t1)
exc.attach(t2)
exc.send('hello')
exc.send('world')
print(exc._subscribers)
exc.detach(t1)
exc.detach(t2)
print(exc._subscribers)


class DisplayMessages:
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))


exc = get_exchange('name')
d = DisplayMessages()
t = Task()
exc.attach(d)
exc.attach(t)
exc.send('aa')

