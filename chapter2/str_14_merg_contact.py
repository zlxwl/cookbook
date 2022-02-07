# 合并序列和可迭代对象，使用join方法
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(''.join(parts))


# += 每次执行时会创建一个新的str对象。效率要比join()很多, 使用生成器
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))


# 代码从许多短字符串中构建，应该考虑编写生成器函数，通过yield关键字生成字符串片段。
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicage'

text = ' '.join(sample())
print(text)

with open('str_14.txt', 'w', encoding='utf-8') as f:
    for part in sample():
        f.write(part)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    with open('str_14_2.txt', 'w', encoding='utf-8') as f:
        for part in sample():
            f.write(part)