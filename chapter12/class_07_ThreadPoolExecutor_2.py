# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_07_ThreadPoolExecutor_2.py
# Time       ：2022/3/25 22:47
# Author     ：Zhong Lei
"""
from concurrent.futures import ThreadPoolExecutor
import urllib.request


def fetch_url(url):
    u = urllib.request.urlopen(url=url)
    return u.read()


pool = ThreadPoolExecutor(10)

a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')

x = a.result()
y = b.result()