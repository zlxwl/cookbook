# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_07_ThreadPoolExecutor.py
# Time       ：2022/3/25 21:18
# Author     ：Zhong Lei
"""
from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor


def echo_client(sock: socket, client_addr):
    print('Got connection from', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)

    while True:
        client_sock, client_addr = sock.accept()
        pool.sumbit(echo_client, client_sock, client_addr)

echo_server(('', 15000))