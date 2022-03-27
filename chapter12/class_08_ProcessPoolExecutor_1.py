# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_08_ProcessPoolExecutor_1.py
# Time       ：2022/3/26 15:29
# Author     ：Zhong Lei
"""
import gzip
import glob
import io
from concurrent.futures import ProcessPoolExecutor


def find_robot(filename):
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    with ProcessPoolExecutor as pool:
        for robots in pool.map(find_robot, files):
            all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)