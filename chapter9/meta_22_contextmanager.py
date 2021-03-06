import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


# with timethis('count'):
#     n = 100000000
#     while n > 0:
#         n -= 1


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


if __name__ == '__main__':
    items = [1, 2, 3]
    with list_transaction(items) as working:
        working.append(4)
        working.append(5)
        # raise RuntimeError('oops')
    print(items)