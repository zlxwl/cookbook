from collections import Counter
# 通过counter字典统计
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't",
    'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
]
word_count = Counter(words)
print(word_count.most_common(3))
print(word_count['not'])
print(word_count['eyes'])


# 手动增加计数
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_count[word] += 1
print(word_count['eyes'])

# 作者使用dict.update() 方法。
word_count.update(morewords)
print(word_count)


# counter 对象 支持 +， -
a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
d = a - b
print(d)