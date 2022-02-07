text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.rjust(20, '='))
print(text.center(20, '*'))

# format不仅可以用于str 还可以用于数字和字符串
print(format(text, '>20'))
print(format(text, '*^20'))

'{:>10s} {:>10s}'.format('Hello', 'World')

x = 1.234
print(format(x, '>10'))
print(format(x, '^10.2f'))


