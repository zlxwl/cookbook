def exec_demo():
    a = 10
    loc = locals()
    exec('b=a+10')
    return loc['b']


def exec_demo_2():
    x = 0
    exec('x+=1')
    print(x)


def exec_demo_3():
    x = 0
    loc = locals()
    print(loc)
    exec('x+=1')
    print(loc)
    locals()
    print(loc)


def exec_demo_4():
    a = 13
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)


if __name__ == '__main__':
    # b = exec_demo()
    # exec_demo_2()
    # exec_demo_3()
    exec_demo_4()
