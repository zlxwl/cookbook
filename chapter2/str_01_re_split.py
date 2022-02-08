import re
## 1 （不获取分隔符）
line = 'asdf fjdk; afed, fjek,asdf,    foo'
fields = re.split(r'[;, \s]\s*', line)

## 2 (获取分割符)
line = 'asdf fjdk; afed, fjek,asdf,    foo'
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

## 3 （reformat）
values = fields[::2]
delimiters = fields[1::2]+['']
print(''.join(v+d for v, d in zip(values, delimiters)))

## 4
fields = re.split(r'(?:,|;|\s)\s*', line)
print(fields)
