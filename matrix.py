from math import sqrt


def create_matrix(s):
    n = 1
    while n**2 < len(s):
        n+=1
    x = 0
    matr = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if x >= len(s):
                matr[i][j] = " "
            else:
                matr[i][j] = s[x]
            x += 1
    return matr


def read_matrix(m):
    n = len(m)
    l = [[0 for j in range(n)] for i in range(n)]
    N = n * n
    i = 0
    j = 0
    k = 0
    while k < N:
        l[i][j] = m[k // len(m)][k % len(m)]
        if i <= j + 1 and i + j < n - 1:
            j += 1
        elif i < j and i + j >= n - 1:
            i += 1
        elif i >= j and i + j > n - 1:
            j -= 1
        else:
            i -= 1
        k += 1
    return l


text = str(input("Введите текст"))
a = read_matrix(create_matrix(text))
for i in a:
    print(i)
