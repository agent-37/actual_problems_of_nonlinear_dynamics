from cmath import cos, sin, sqrt
from sympy import sin, cos, Matrix, diff, solve, N, symbols
import numpy as np
from sympy.abc import x, y, z
import matplotlib.pyplot as plt

eps = 1e-8


def func():
    return cos(x - 1) * sin(x ** 2)


def f(num):
    return func().limit(x, num)


def d_f(num, h):
    return (f(num + h) - f(num)) / h


def dd_f(num, h):
    return (f(num + h) - 2 * f(num) + f(num - h)) / h


def print_roots(a, b, h, dc):
    rf, rdf, rddf, points = [], [], [], []
    left = a
    while left < b:
        rf.append(f(left))
        rdf.append(d_f(left, h))
        rddf.append(dd_f(left, h))
        points.append(left)
        left += dc
    plt.plot(points, rf)
    plt.plot(points, rdf)
    plt.plot(points, rddf)
    plt.legend(('f(x)', 'f\'(x)', 'f\'\'(x)'))
    plt.show()


a, b, h, dc = map(float, input("Введите отрезок a,b,h,dc\n").split())
print_roots(a, b, h, dc)
