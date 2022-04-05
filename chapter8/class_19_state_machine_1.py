# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : class_19_state_machine_1.py
# Time       ：2022/4/5 0:49
# Author     ：Zhong Lei
"""
class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, new_state):
        self._state = new_state

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


class ConnectionStates:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


class ClosedConnectionState(ConnectionStates):
    @staticmethod
    def read(conn):
        raise RuntimeError('not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('already closed')


class OpenConnectionState(ConnectionStates):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('already closed')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


if __name__ == '__main__':
    c = Connection()
    print(c._state)
    c.open()
    c.read()