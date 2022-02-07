text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'),
          ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z][a-zA-z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pattern = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pattern.scanner('foo = 42')
print(scanner.match().groups())

from collections import namedtuple
Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for token in generate_tokens(master_pattern, 'foo = 42'):
    # print(token)
    pass

# 使用生成器表达式进行过滤
tokens = [token for token in generate_tokens(master_pattern, text)
          if token.type != 'WS']
for token in tokens:
    print(token)


# 注意包含形成的字串的情况。<= 放在<的前面。

PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pattern = re.compile('|'.join([PRINT, NAME]))

for token in generate_tokens(master_pattern, text='printer'):
    print(token)

