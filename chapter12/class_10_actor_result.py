# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_10_actor_result.py
# Time       ：2022/3/27 20:28
# Author     ：Zhong Lei
"""
from queue import Queue
from threading import Event, Thread


class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if not msg:
            raise ActorExit
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._teminate = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def join(self):
        self._teminate.wait()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._teminate.set()

    def run(self):
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got: ', msg)


# p = PrintActor()
# p.start()
# p.send('hello')
# p.send('world')
# p.close()
# p.join()


class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'do_' + tag)(*payload)

    def do_A(self, x):
        print('running A', x)

    def do_B(self, x, y):
        print('running B', x, y)


t = TaggedActor()
t.start()
t.send(('A', 1))
t.send(('B', 2, 3))
t.close()
t.join()


class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


w = Worker()
w.start()
r = w.submit(pow, 2, 3)
w.close()
w.join()
print(r.result())



