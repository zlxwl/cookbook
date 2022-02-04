text = 'yeah, but no, but yeah, but no, but yeah'
other = text.replace('yeah', 'yep')
print(other)

# re.sub('查找的模式'， '要替换为的模式', 文本)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text))

# patten = re.compile()  patten.sub('', '', text)
pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
print(pattern.sub(r'\3-\2-\1', text))


# 将替换模式转替换为函数
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(pattern.sub(change_date, text))

# 返回替换的次数
result, n = pattern.subn(r'\3-\2-\1', text)
print(n)
print(result)