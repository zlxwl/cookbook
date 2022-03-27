# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_07_ThreadPoolExecutor_1.py
# Time       ：2022/3/25 22:27
# Author     ：Zhong Lei
"""
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue


def echo_client(q: Queue):
    sock, client_addr = q.get()
    print('Got connection from', client_addr)

    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('client closed connection')
    sock.close()


def echo_server(addr, nworkers):
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q, ))
        t.daemon = True
        t.start()

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))


echo_server(('', 15000), 128)


