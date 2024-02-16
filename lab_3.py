from cmath import cos
from sympy import cos
from sympy.abc import x

eps = 1e-8


def sum_pow(dots, _pow):
    sum = 0
    for i in dots:
        sum += i[0] ** _pow
    return sum


def create_poly(n):
    poly = []
    for i in range(n + 1):
        poly.append(0)
    return poly


def find_matrix(dots, N):
    buf, matrix = [], []
    for i in range(N):
        buf = []
        for i in range(N):
            buf.append(0)
        matrix.append(buf)

    for i in range(N * 2 - 1):
        if i == 0:
            el = len(dots)
        else:
            el = sum_pow(dots, i)

        for j in range(min(i + 1, N * 2 - i - 1)):
            matrix[max(0, i - N + 1) + j][max(0, N - i - 1) + j] = el
    return matrix


def sum_pow_y(dots, _pow):
    sum = 0
    for i in dots:
        sum += i[1] * i[0] ** _pow
    return sum


def find_b(dots, N):
    b = []
    for i in range(N):
        b.append(sum_pow_y(dots, i))
    return b


def read_dots(f_file, N):
    dots = []
    for i in range(N):
        a, b = map(float, f_file.readline().split())
        dots.append((a, b))
    return dots


def gaus(matrix, b):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[j], matrix[i] = matrix[i], matrix[j]
                    break
        k = matrix[i][i]
        if k == 0:
            return None
        b[i] /= k
        for j in range(i + 1, n):
            matrix[i][j] /= k
        for j in range(i + 1, n):
            k = matrix[j][i]
            if k != 0:
                b[j] -= k * b[i]
                for h in range(i, n):
                    matrix[j][h] -= k * matrix[i][h]
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            b[j] -= b[i] * matrix[j][i]
            matrix[j][i] = 0
    return b


n = int(input('Введите степень многочлена\n'))


f_file = open("input.txt", 'r')

N = int(f_file.readline())

dots = read_dots(f_file, N)
b = find_b(dots, n + 1)
matrix = find_matrix(dots, n + 1)
print(matrix)
print(b)
poly = gaus(matrix,b)
print(poly)