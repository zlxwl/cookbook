# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : gen_iter_13_pipline.py
# Time       ：2022/2/23 22:25
# Author     ：Zhong Lei
"""
import os
import bz2
import gzip
import fnmatch
import re


def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(name, path)


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    for it in iterators:
        yield from it


def gen_grep(patten, lines):
    pat = re.compile(patten)
    for line in lines:
        if pat.search(line):
            yield pat


lognames = gen_find('access-log*', 'chapter4')
print(list(lognames))
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for x in pylines:
    print(x)
