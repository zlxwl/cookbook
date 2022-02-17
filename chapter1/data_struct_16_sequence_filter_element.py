my_list = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in my_list if n > 0])

pos = (n for n in my_list if n > 0)
for x in pos:
    print(x)


# 过滤规则复杂就使用filter
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)


# 过滤的同时处理数据
import math
print([math.sqrt(n) for n in my_list if n > 0])

print([n if n > 0 else 0 for n in my_list])

clip_neg = [n if n > 0 else 0 for n in my_list]
clip_pos = [n if n < 0 else 0 for n in my_list]


# 使用itertools.compare(), 1. [n > 5 for n in counts] -> [True, False, ...]  2. compress(add, boolean_seq)
address = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4081 N BROADWAY',
    '1039 W GRANVILLE'
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more = [n > 5 for n in counts ]
print(more)
print(list(compress(address, more)))
