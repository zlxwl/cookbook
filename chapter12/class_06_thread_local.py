# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_06_thread_local.py
# Time       ：2022/3/24 22:38
# Author     ：Zhong Lei
"""
import threading
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')

        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock


def t_con(conn: LazyConnection):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8198), b''))
    print('Got {} bytes'.format(len(resp)))


if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))
    t1 = threading.Thread(target=t_con, args=(conn,))
    t2 = threading.Thread(target=t_con, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()



