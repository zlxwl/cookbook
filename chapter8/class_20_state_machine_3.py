# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_20_state_machine_3.py
# Time       ：2022/4/5 12:21
# Author     ：Zhong Lei
"""
class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, state):
        self.__class__ = state

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('not open')

    def write(self, data):
        raise RuntimeError('not open')

    def open(self):
        return self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('already closed')


class OpenConnection(Connection):
    def read(self):
        print('reading')

    def write(self, data):
        print('writing {}'.format(data))

    def open(self):
        raise RuntimeError('already open')

    def close(self):
        return self.new_state(ClosedConnection)


if __name__ == '__main__':
    c = Connection()
    # c.read()
    c.open()
    c.read()
    c.write('data')
    c.close()
    