# remove whitespace
s = ' hello world \n'
print(s.strip())

print(s.lstrip())
print(s.rstrip())

# remove character
t = '-----hello====='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))
print(t.strip('=-'))


# 不会对字符串中间的任何文本起作用
s = ' hello    world   \n'
s = s.strip()
print(s)


# 使用replace或者re.sub
print(s.replace(' ', ''))


# re.sub
import re
print(re.sub('\s+', '', s))


# 迭代的同时去除文本字符
filename = 'a'
with open(filename) as f:
    # 创建迭代器，控制内存
    lines = (line.strip() for line in f)
    for line in lines:
        pass
