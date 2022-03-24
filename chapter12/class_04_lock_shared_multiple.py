import threading


class SharedCounter:
    _lock = threading.Lock()

    def __init__(self, initial_value=0):
        self._initial_value = initial_value

    def incr(self, delta=1):
        with SharedCounter._lock:
            self._initial_value += delta

    def decr(self, delta=1):
        with SharedCounter._lock:
            self._initial_value -= delta


from threading import Semaphore
import urllib.request

_fetch_url_sema = Semaphore(5)


def fetch_url(url):
    with _fetch_url_sema:
        return urllib.request.urlopen(url)