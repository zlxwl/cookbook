# 使用str。
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no')) # search the first location of the occurrence


# 使用正则表达式。
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
if re.match(r'\d+/\d+/\d+', text1):# \d+ means one or more digits.
    print('yes')
else:
    print('no')


# 使用正则表达式对同一种模式做多次匹配。
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1): # match 在字符串的开头对同一种模式做多匹配。
    print('yes')
else:
    print('no')


# 找到所有匹配
text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
print(datepat.findall(text))


# 将部分模式用括号包起来的方式引入捕获组。
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(1))
print(m.group(2))
print(m.groups()) # 返回的是元祖。
month, date, year = m.groups()


# findall
text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datapat.findall(text)) # List[tuple[str]]

for mon, day, year in datapat.findall(text):
    print('{}-{}-{}'.format(year, mon, day))

for m in datapat.finditer(text):
    print(m.groups())


# 对文本做匹配的方法 1.pattern = re.compile(); 2. re.match() re.findall() re.finditer()查找。
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))


