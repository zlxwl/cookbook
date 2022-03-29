import queue
import socket
import os


class PollableQueue(queue.Queue):
    def __init__(self):
        super(PollableQueue, self).__init__()
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)

            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def put(self, item, block=True, timeout=None):
        super().put(item)
        self._putsocket.send(b'x')

    def get(self, block=True, timeout=None):
        self._getsocket.recv(1)
        return super().get()

    def fileno(self):
        return self._getsocket.fileno()


import select
import threading


def consumer(queues: queue.Queue):
    while True:
        can_read, _, _ = select.select(queues, [], [])
        for r in can_read:
            item = r.get()
            print('Got:', item)


# 同时轮询socket和queues
# def event_loop(sockets, queues):
#     while True:
#         polling with a timeout
        # can_read, _, _ = select.select(sockets, [], [], 0.01)
        # for r in can_read:
        #     handle_read(r)
        # for q in queues:
        #     if not q.empty():
        #         item = q.get()
        #         print('Got:', item)


if __name__ == '__main__':
    q1 = PollableQueue()
    q2 = PollableQueue()
    q3 = PollableQueue()
    t = threading.Thread(target=consumer, args=([q1, q2, q3], ))
    t.daemon = True
    t.start()

    q1.put(1)
    q2.put(10)
    q3.put('hello')
    q2.put(5)
    t.join()


