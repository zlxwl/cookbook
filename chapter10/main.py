# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : main.py
# Time       ：2022/4/14 20:45
# Author     ：Zhong Lei
"""
import sys
sys.path.append('.')
from chapter10.module_02__all__ import *
from chapter9 import meta_01_functools_wraps


if __name__ == '__main__':
    grok()
    spam()
    meta_01_functools_wraps.countdown(10000000)
