from cmath import cos, sin
from sympy import sin, cos, Matrix, diff, solve, N
import numpy as np
from sympy.abc import x, y
import matplotlib.pyplot as plt

eps = 1e-8


def func():
    return cos(x - 1) *sin(x**2 )


def f(num, c):
    return func().limit(y, c).limit(x, num)


def dfunc_dc():
    return diff(func, y)


def dfunc_dx():
    return diff(func, x)


def df_x(num, c):
    return  diff(cos(x - 1) *sin(x**2) , x).limit(y, c).limit(x, num)


def df_c(num, c):
    return diff(cos(x - 1) *sin(x**2) , y).limit(y, c).limit(x, num)


def recurent_find(a, b, c):
    if abs(b - a) < eps:
        return (a + b) / 2
    if f(a, c) * f((a + b) / 2, c) <= 0:
        return recurent_find(a, (a + b) / 2, c)
    else:
        if f((a + b) / 2, c) * f(b, c) <= 0:
            return recurent_find((a + b) / 2, b, c)
        else:
            return None


def find_list_ans(N, a, b, c):
    ans = []
    for i in range(N):
        cur = 0
        # print(i)
        if f(a + (b - a) / N * i, c) * f(a + (b - a) / N * (i + 1), c) <= 0:
            cur = recurent_find(a + (b - a) / N * i, a + (b - a) / N * (i + 1), c)
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


def find_aswers(a, b, c):
    N = 100
    cur = find_list_ans(N, a, b, c)
    next = find_list_ans(2 * N, a, b, c)
    while not check(cur, next) and N < 1e8:
        cur = next
        N *= 2
        next = find_list_ans(N, a, b, c)
        print(N)
    # print(len(cur))
    # for i in cur:
    #     print(i, end=' ')
    if N >= 1e8:
        return None
    else:
        return cur


def find_roots(a, b, alpha, beta, dc):
    res = find_aswers(a, b, alpha)
    # print(res)
    matrix = []
    for i in range(len(res)):
        buf = [res[i]]
        matrix.append(buf)

    for i in range(len(matrix)):
        c_0 = alpha
        x_0 = matrix[i][0]
        # print(df_x(x_0, c_0))
        while c_0 < beta:
            if abs(df_x(x_0, c_0)) < eps * 100:
                break
            x_0 = x_0 - df_c(x_0, c_0) / df_x(x_0, c_0)
            matrix[i].append(x_0)
            c_0 += dc
    return matrix


def print_roots(matrix, a, dc):
    for i in range(len(matrix)):
        buf = []
        for j in range(len(matrix[i])):
            buf.append(a + dc * j)
        plt.plot(buf, matrix[i])
    plt.show()


a, b, alpha, beta, dc = map(float, input("Введите отрезок a,b,alpha,beta, dc\n").split())
print_roots(find_roots(a,b,alpha,beta,dc),a,dc)
# find_roots(a, b, alpha, beta, dc)
# print(diff(cos(x - 1) * y ** 2, y).limit(y,2).limit(x,5))
