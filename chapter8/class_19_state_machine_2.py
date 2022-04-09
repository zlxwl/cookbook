# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_19_state_machine_2.py
# Time       ：2022/4/5 1:16
# Author     ：Zhong Lei
"""
class State:
    def __init__(self):
        self.new_state(State_A)

    def new_state(self, state):
        self.__class__ = state

    def action(self, x):
        raise NotImplementedError()


class State_C(State):
    def action(self, x):
        # do action for C
        self.new_action(State_A)


class State_B(State):
    def action(self, x):
        # do action for B
        self.new_action(State_C)


class State_A(State):
    def action(self, x):
        # do action for A
        self.new_state(State_B)


class State:
    def __init__(self):
        self.state = 'A'

    def action(self):
        if self.state == 'A':
            # do action for b
            self.state = 'B'
        elif self.state == 'B':
            # do action for b
            self.state = 'C'
        elif self.state == 'C':
            # do action for c
            self.state = 'A'