a = [1, 2, 3, 4]
b = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

def f(a, b, c, d, e = 5, f = 6):
    print(a, b, c, d, end="s")


def g(*args, **kwargs):
    print(args)
    print(kwargs.values())
    print(kwargs.keys())

g(1, 2, 3, 5, 4, a = 8, b = 3, c = 7)