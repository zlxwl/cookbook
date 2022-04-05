# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_19_state_machine.py
# Time       ：2022/4/4 18:57
# Author     ：Zhong Lei
"""
class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('NOT OPEN')
        print('reading')

    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('NOT OPEN')
        print('writing {}'.format(data))

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('already opened')
        self.state == 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('already closed')
        self.state = 'CLOSED'