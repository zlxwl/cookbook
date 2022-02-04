s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)



import unicodedata
import sys
# unicode: None 映射表
chm_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
# 将unicode组合形式，转化为分离形式
b = unicodedata.normalize('NFD', a)
print(b)
# 通过装话形式删除所有重音符号
print(b.translate(chm_chrs))


# translate
digitmap = {
    c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode)
    if unicodedata.category(chr(c)) == 'Nd'
}
print(digitmap)
print(len(digitmap))

x = '\u0661\u0662\u0663'
print(x.translate(digitmap))


# encode和decode方法
b = unicodedata.normalize('NFD', a)
print(b)
print(b.encode('ascii', 'ignore').decode('ascii'))
