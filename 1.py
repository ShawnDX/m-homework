import math


def f(x):
    f = x ** 2 + 3 * x + 3
    return f


def g(x):
    return math.sin(x) + 2 * (x - 2) / (x + 1)


def h(x):
    return math.sinh(x + 1) - math.exp(2 * x)


def composition(outer_function, inter_function, value):
    return outer_function(inter_function(value))


print("The compositiuon g(f(x)) when x =5.0 equals " + str(composition(g, f, 5.0)))
