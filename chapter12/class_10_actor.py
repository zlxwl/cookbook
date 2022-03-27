# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_10_actor.py
# Time       ：2022/3/26 23:09
# Author     ：Zhong Lei
"""
from queue import Queue
from threading import Thread, Event

class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminate = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def join(self):
        self._terminate.wait()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminate.set()

    def run(self):
        while True:
            self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got:', msg)


p = PrintActor()
p.start()
p.send('Hello')
p.send('world')
p.close()
p.join()


def print_actor():
    while True:
        try:
            msg = yield
            print('Got:', msg)
        except GeneratorExit:
            print('actor terminate')

p  = print_actor()
next(p)
p.send('hello')
p.send('world')

