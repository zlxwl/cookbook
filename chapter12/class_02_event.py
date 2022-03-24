from threading import Event, Thread
import time


def countdown(n, start_event: Event):
    print('countdown starting')
    start_event.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(0.5)

start_event = Event()
print('launching countdown')
t = Thread(target=countdown, args=(5, start_event))
t.start()

start_event.wait()
print('countdown is running')


