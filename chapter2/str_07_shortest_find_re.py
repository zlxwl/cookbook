import re
pattern = re.compile(r'\"(.*)\"')
text1 = 'computer says "no."'
print(pattern.findall(text1))

# 正则表达式*使用的是最长匹配策略，要最短匹配策略需要在*后面加?
text2 = 'Computer says "no." Phone says "yes."'
print(pattern.findall(text2))

pattern = re.compile(r'\"(.*?)\"')
print(pattern.findall(text2))


