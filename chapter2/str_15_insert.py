# format 模拟
s = '{name} has {n} message.'
print(s.format(name='Guido', n=37))

# 使用format_map()和vars()
name = 'Guido'
n = 37
print(s.format_map(vars()))


# vars() obj
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
print(s.format_map(vars(a)))

# 处理确实值的情况
class safesub(dict):
    def __missing__(self, key):
        return '(' + key + ')'

del n
print(s.format_map(safesub(vars())))

# frame hacking
import sys
def sub(text: str):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

# other methods
name = 'Guido'
n = 37
import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))

# 使用format()，format_map方法是最现代化的方式, 对齐，填充，数值格式化。