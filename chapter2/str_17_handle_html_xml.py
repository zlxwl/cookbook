s = 'Elements are written as "<tag>text</tag>".'
import html
print(html.escape(s))
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))


# 替换html文本中的实体
from html.parser import HTMLParser
s = 'Spicy &quot;Jalape&#241;o&quot.'
h = HTMLParser()
print(h.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))