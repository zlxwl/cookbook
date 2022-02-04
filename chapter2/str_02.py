# 单个字符串做开头或者末尾的字符串匹配
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('.txt'))


# 在.endswith()后添加元组可以增加匹配到的数量
import os
file_names = os.listdir('.')
print([file.endswith(('.py', '.txt')) for file in file_names])
print([name for name in file_names if name.endswith(('.py', '.txt'))])


from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# 检查目录中有特定文件的出现
if any(name.startswith(('.c', '.h')) for name in os.listdir('.')):
    pass


# 使用正则表达式来匹配
import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))