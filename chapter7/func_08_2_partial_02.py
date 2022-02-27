# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : func_08_2_partial_02.py
# Time       ：2022/2/27 23:33
# Author     ：Zhong Lei
"""
from functools import partial
from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

# serv = TCPServer(('', 15000), EchoHandler)
serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'Received'))
serv.serve_forever()


# 另外一种实现方式
# points.sort(key=lambda p: distance(pt, p))
# serv = TCPServer(('', 15000), lambda *args, **kwargs: EchoHandler(*args, ack=b'Received', **kwargs))
# p.apply_async(add, (3, 4), callback = lambda result: output_result(result, log))