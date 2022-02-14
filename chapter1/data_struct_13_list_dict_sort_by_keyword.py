# 使用itemgetter对列表字典排序
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_name = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_name)
print(rows_by_uid)

row_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(row_by_lfname)

