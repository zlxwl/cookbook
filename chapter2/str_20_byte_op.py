# 字节字符串
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# 字节数组
data = bytearray(b'Hello World')
print(data[:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# 使用正则表达式
import re
data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]', data))


# 字节字符串索引操作返回整数而不是单独字符
a = 'Hello World'
print(a[0])
b = b'Hello World'
print(b[0])

# 字节字符串必须通过decode方法才能被美观的打印出来
s = b'Hello World'
print(s)
print(s.decode())

# decode后才能支持格式化
print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

with open('jalape\xf1o.txt', 'w') as f:
    f.write('Scipy')

import os
print(os.listdir('.'))
print(os.listdir(b'.'))
