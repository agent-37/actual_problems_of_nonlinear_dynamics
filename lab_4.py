from cmath import cos, sin, sqrt
from sympy import sin, cos, Matrix, diff, solve, N, symbols
import numpy as np
from sympy.abc import x, y, z, t
import matplotlib.pyplot as plt

eps = 1e-8


def func():
    return Matrix([cos(x)*t, sin(y) + x])


def fk(num1, num2, t1):
    return func().limit(x, num1).limit(y, num2).limit(t, t1)[0]


def fq(num1, num2, t1):
    return func().limit(x, num1).limit(y, num2).limit(t, t1)[1]


def find_dots(x_0_1, x_0_2):
    t_0 = 0
    h = 0.05
    points_1 = []
    points_2 = []
    for i in range(100):
        k1 = fk(x_0_1, x_0_2, t_0)
        q1 = fq(x_0_1, x_0_2, t_0)
        k2 = fk(x_0_1 + h * k1 / 3, x_0_2 + h * q1 / 3, t_0 + h / 3)
        q2 = fq(x_0_1 + h * k1 / 3, x_0_2 + h * q1 / 3, t_0 + h / 3)
        k3 = fk(x_0_1 - h * k1 / 3 + h * k2, x_0_2 - h * q1 / 3 + h * q2, t_0 + 2 / 3 * h)
        q3 = fq(x_0_1 - h * k1 / 3 + h * k2, x_0_2 - h * q1 / 3 + h * q2, t_0 + 2 / 3 * h)
        k4 = fk(x_0_1 + h * k1 - h * k2 + h * k3, x_0_2 + h + q1 - h * q2 + h * q3, t_0 + h)
        q4 = fq(x_0_1 + h * k1 - h * k2 + h * k3, x_0_2 + h + q1 - h * q2 + h * q3, t_0 + h)
        x_0_1 += h / 8 * (k1 + 3 * k2 + 3 * k3 + k4)
        x_0_2 += h / 8 * (q1 + 3 * q2 + 3 * q3 + q4)
        # print(x_0_1, x_0_2)
        t_0 += h
        points_1.append(x_0_1)
        points_2.append(x_0_2)
        # print(i)
    res = []
    res.append(points_1)
    res.append(points_2)
    return res


def print_dots(res):
    plt.plot(res[1], res[0])
    plt.show()


x_0_1, x_0_2 = map(float, input('Введите начальное значение x_0\n').split())
print_dots(find_dots(x_0_1, x_0_2))
