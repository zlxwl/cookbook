from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))

# 通配符
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])


# 使用通配符匹配，比正则表达式更容易记忆. 介于简单的字符串匹配和全功能的正则表达式之间。
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]
from fnmatch import fnmatchcase
print([add for add in addresses if fnmatchcase(add, '*ST')])
print([add for add in addresses if fnmatchcase(add, '54[0-9][0-9] *CLARK*')])