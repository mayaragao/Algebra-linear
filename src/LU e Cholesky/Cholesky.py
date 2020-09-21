from math import sqrt
import numpy as np


def cholesky(A):

    n = np.shape(A)[0]
    L = np.zeros((n, n))

    boo = simetrica(A)
    if boo == False:
        return (L, boo)

    for i in np.arange(n):
        for k in np.arange(i+1):
            soma = 0
            for j in np.arange(k):
                soma += (L[i, j] * L[k, j])

            if (i == k):
                L[i, k] = ((A[i, i] - soma) ** 0.5)
            else:
                L[i, k] = ((A[i, k] - soma) / L[k, k])
    return (L, boo)  # retorna matriz L e booleano que diz se é simétrica


def transposta(A):
    n = np.shape(A)[0]
    L = np.zeros((n, n))

    for i in np.arange(n):
        for j in np.arange(n):
            L[j, i] = A[i, j]
    return L


def simetrica(A):
    n = np.shape(A)[0]
    m = np.shape(A)[1]
    if (n != m):
        return False
    At = transposta(A)

    for i in np.arange(n):
        for j in np.arange(n):
            if (At[i, j] != A[i, j]):
                return False

    return True
