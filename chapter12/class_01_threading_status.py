from threading import Thread
import time
from socket import socket


class CountdownTask:
    def __init__(self):
        self._running = True

    def _terminate(self):
        self._running = False

    def run(self, n):
        while n > 0 and self._running:
            print('T-minus', n)
            n -= 1
            time.sleep(0.5)
#
#
c = CountdownTask()
t = Thread(target=c.run, args=(5, ))
t.start()
c._terminate()
t.join()

#
# class IOTask:
#     def terminate(self):
#         self._running = False
#
#     def run(self, socket):
#         socket.settimeout(5)
#         while self._running:
#             try:
#                 data = socket.recv(1000)
#                 break
#             except socket.timeout:
#                 continue
#         return
#
#
class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(0.5)

import multiprocessing
c = CountdownTask()
p = multiprocessing.Process(target=c.run, args=(5,))
p.start()
p.join()