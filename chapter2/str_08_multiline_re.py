import re
# . 无法匹配换行符
text1 = '/* this is comment */'
text2 = '''/* this is a 
            multiline comment */
            '''
pattern = re.compile(r'/\*(.*?)\*/')
print(pattern.findall(text1))
# . 无法匹配换行符
print(pattern.findall(text2))

# 使用(?:.|\n) 指定了一个非捕获组（只做匹配，但不捕获结果，不分配组号）
pattern = re.compile(r'/\*((?:.|\n)*?)\*/')
print(pattern.findall(text2))

# 使用re.DOTALL
pattern = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(pattern.findall(text2))
