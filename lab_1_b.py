from cmath import cos, sin, sqrt
from sympy import sin, cos, Matrix, diff, solve, N, symbols
import numpy as np
from sympy.abc import x, y, z
import matplotlib.pyplot as plt

eps = 1e-3
ch_eps = 1e-3

def func():
    return sin(10*z)*(z ** 4 + z ** 2 + 1)

def f(num):
    return func().limit(z, num)

def find_next_z(z_n):
    return z_n - f(z_n) / diff(sin(10*z)*(z ** 4 + z ** 2 + 1), z).limit(z, z_n)

def check(roots, z_0):
    for i in roots:
        if dist(i, z_0) < ch_eps:
            return 0
    return 1

def dist(a, b):
    a = complex(a)
    b = complex(b)
    return sqrt((a.real - b.real) * (a.real - b.real) + (a.imag - b.imag) * (a.imag - b.imag)).real

def find_roots(a, dc):
    x = -a
    roots = []
    while x < a:
        y = -a
        while y < a:
            z_0 = complex(x, y)
            next = complex(find_next_z(z_0))
            while dist(next, z_0) > eps:
                z_0 = complex(next)
                next = complex(find_next_z(z_0))
            if check(roots, z_0):
                roots.append(z_0)
            y += dc
        x += dc
    # print(x)
    return roots

def print_all(roots,a):
    for i in roots:
        if abs(i.real)<=a and abs(i.imag)<=a:
            plt.plot(i.real,i.imag, 'bo')
    plt.show()

a, dc = map(float, input("Введите отрезок a, dc\n").split())
print(find_roots(a, dc))
print_all(find_roots(a,dc),a)