import time


class timethis:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.name, end - self.start))


with timethis('count'):
    n = 1000000
    while n > 0:
        n -= 1


