from cmath import cos, sin
from sympy import sin, cos, Matrix
import numpy as np
from sympy.abc import x, y

eps = 1e-8


def func():
    return cos(x - 1) * sin(x ** 2)


def f(num):
    return func().limit(x, num)


def recurent_find(a, b):
    if abs(b - a) < eps:
        return (a + b) / 2
    if f(a) * f((a + b) / 2) <= 0:
        return recurent_find(a, (a + b) / 2)
    else:
        if f((a + b) / 2) * f(b) <= 0:
            return recurent_find((a + b) / 2, b)
        else:
            return None


def find_list_ans(N, a, b):
    ans = []
    for i in range(N):
        cur = 0
        # print(i)
        if f(a + (b - a) / N * i) * f(a + (b - a) / N * (i + 1)) <= 0:
            cur = recurent_find(a + (b - a) / N * i, a + (b - a) / N * (i + 1))
        if cur is not None and cur != 0:
            ans.append(cur)
    return ans


def check(cur, next):
    # print('zdec')
    if len(cur) != len(next):
        return 0
    for i in range(len(cur)):
        if abs(cur[i] - next[i]) > eps * 3:
            return 0
    return 1


def find_aswers(a, b):
    N = 1000
    cur = find_list_ans(N, a, b)
    next = find_list_ans(2 * N, a, b)
    while not check(cur, next) and N < 1e8:
        cur = next
        N *= 2
        next = find_list_ans(N, a, b)
        print(N)
    # print(len(cur))
    # for i in cur:
    #     print(i, end=' ')
    if N >= 1e8:
        return None
    else:
        return cur


a, b = map(int, input("Введите отрезок a,b\n").split())
res = find_aswers(a, b)
for i in res:
    print(i)
