# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_18_cls_class.py
# Time       ：2022/4/4 18:39
# Author     ：Zhong Lei
"""
def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(cls, key):
        print('getting key {}'.format(key))
        return cls_getitem(cls, key)

    def __setitem__(cls, key, value):
        print('setting {}={!r}'.format(key, value))
        return cls_setitem(cls, key, value)

    def __delitem__(cls, instence):
        print('deleting {}'.format(instence))
        return cls_delitem(cls, instence)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggerDict(dict):
    pass


if __name__ == '__main__':
    d = LoggerDict()
    d['a'] = 1
    print(d['a'])