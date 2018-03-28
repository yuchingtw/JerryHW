#使用*args加分
def add(*args):
    return sum(args)

def sub(*args):
    return args[0] - args[1]

def mul(*args):
    temp = 1
    for i in args:
        temp *= i
    return temp

def div(*args):
    return args[0] / args[1]

def calc(str, *args):
    dic = {'+' : add, '-' : sub, '*': mul, '/': div}
    return dic[str](*args)