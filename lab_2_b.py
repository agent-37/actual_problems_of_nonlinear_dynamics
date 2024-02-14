from cmath import cos, sin, sqrt
from sympy import sin, cos, Matrix, diff, solve, N, symbols
import numpy as np
from sympy.abc import x, y, z
import matplotlib.pyplot as plt

eps = 1e-8


def func():
    return cos(x - 1)


def f(num):
    return func().limit(x, num)


def int_f(a, b):
    if a == b:
        return 0
    return (f(a) + 4 * f((a + b) / 2) + f(b)) * ((b - a) / 6)


def print_roots(a, b, N, h):
    rf, F, points = [], [], []
    left = a
    sum = 0
    pos = a
    while left < b:
        rf.append(f(left))
        while abs(left - pos) > (b - a) / N:
            sum += int_f(pos, pos + (b - a) / N)
            pos += (b - a) / N
        # print(sum)
        F.append(sum + int_f(pos, left))
        points.append(left)
        left += h
    # print(rf)
    # print(F)
    plt.plot(points, rf)
    plt.plot(points, F)
    plt.legend(('f(x)', 'F(x)'))
    plt.show()


a, b, N, h = map(float, input("Введите отрезок a,b,N,h\n").split())
print_roots(a, b, N, h)
