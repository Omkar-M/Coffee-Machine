def f1(x):
    return x * x + 1


def f2(x):
    return 1 / (x * x)


def f3(x):
    return x * x - 1


def f(x):
    if x <= 0:
        return f1(x)
    if 0 < x < 1:
        return f2(x)
    return f3(x)
