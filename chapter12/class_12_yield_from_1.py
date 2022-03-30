# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_12_yield_from_1.py
# Time       ：2022/3/28 21:48
# Author     ：Zhong Lei
"""
from collections import deque


class ActorSchedule:
    def __init__(self):
        self._actors = {}
        self._meg_queue = deque()

    def new_actor(self, name, actor):
        self._meg_queue.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._meg_queue.append((actor, msg))

    def run(self):
        while self._meg_queue:
            actor, msg = self._meg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass


def printer():
    while True:
        msg = yield
        print('Got', msg)


def counter(sched):
    while True:
        n = yield
        if n == 0:
            break
        sched.send('printer', n)
        sched.send('counter', n-1)


if __name__ == '__main__':
    sched = ActorSchedule()
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

    sched.send('counter', 10)
    sched.run()
