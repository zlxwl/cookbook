from threading import Thread
import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(3)

t = Thread(target=countdown, args=(5, ), daemon=True)
t.start()
t.join()
if t.is_alive():
    print('still_alive')
else:
    print('completed')
