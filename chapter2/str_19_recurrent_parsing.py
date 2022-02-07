# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : str_19_recurrent_parsing.py
# Time       ：2022/2/7 21:11
# Author     ：Zhong Lei
"""
import re
import collections

# token specification
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>()'
RPAREN = r'(?P<RPAREN>))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_text(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        token = Token(m.lastgroup, m.group())
        if token.type != 'WS':
            yield token


class ExpressionEvaluator:
    def parse(self, text):
        self.tokens = generate_text(text)
        self.token = None
        self.next_token = None
        self._advance()
        return self.expr()

    def _advance(self):
        'Advanced one token ahead'
        self.token, self.next_token = self.next_token, next(self.tokens, None)

    def _accept(self, token_type):
        'Test and consume the next token if it matched token_type'
        if self.next_token and self.next_token.type == token_type:
            self._advance()
            return True
        else:
            return False

    def _expect(self, token_type):
        'Consume next token if matches token_type or raise SyntaxError'
        if not self._accept(token_type):
            raise  SyntaxError('Expected' + token_type)

    def expr(self):
        "expression ::= term { ('+'|'-' term }*"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.token.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'\'/') factor }*"
        termval = self.fator()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.token.type
            right = self.fator()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def fator(self):
        "factor ::= NUM | ( expr )"
        if self._accept('NUM'):
            return int(self.token.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER OR LAPREN')


class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.token.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval

    def term(self):
        termval = self.fator()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.token.type
            right = self.term()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def fator(self):
        if self._accept('NUM'):
            return int(self.token.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER OR LPAREN')


def descent_parser():
    e = ExpressionEvaluator()
    print(e.parse(text='2'))
    print(e.parse(text='2+3'))
    print(e.parse(text='2+3*4'))
    print(e.parse(text='2+3*'))


def descent_tree_builder():

    e = ExpressionTreeBuilder()
    print(e.parse(text='2'))
    print(e.parse(text='2+3'))
    print(e.parse(text='2+3*4'))
    print(e.parse(text='2+3*'))


if __name__ == '__main__':
    descent_tree_builder()