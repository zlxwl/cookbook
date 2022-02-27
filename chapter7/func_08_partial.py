# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_08_partial.py
# Time       ：2022/2/27 22:47
# Author     ：Zhong Lei
"""
# from functools import partial
# points = [(1, 2), (3, 4), (5, 6), (7, 8)]
#
# import math
# def distance(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return math.hypot(x2 - x1, y2 - y1)
#
# pt = (4, 3)
# points.sort(key=partial(distance, pt))
# print(points)


def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


def add(x, y):
    return x + y


if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()

