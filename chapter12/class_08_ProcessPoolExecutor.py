# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_08_ProcessPoolExecutor.py
# Time       ：2022/3/26 15:16
# Author     ：Zhong Lei
"""
import io
import gzip
import glob


def find_robots(filename):
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
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    all_robots = find_all_robots('logs')
    for ipaddr in all_robots:
        print(ipaddr)