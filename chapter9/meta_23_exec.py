def exec_demo():
    a = 10
    loc = locals()
    exec('b=a+10')
    return loc['b']


if __name__ == '__main__':
    b = exec_demo()
    print(b)


