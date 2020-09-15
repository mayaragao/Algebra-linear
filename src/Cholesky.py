from math import sqrt
import numpy as np


def cholesky(A):
    n = np.shape(A)[0]
    L = np.zeros((n, n))

    for i in np.arange(n):
        for k in np.arange(i+1):
            soma = 0
            for j in np.arange(k):
                soma += (L[i, j] * L[k, j])

            if (i == k):
                L[i, k] = ((A[i, i] - soma) ** 0.5)
            else:
                L[i, k] = ((A[i, k] - soma) / L[k, k])
    return L


def transposta(A):
    n = np.shape(A)[0]
    L = np.zeros((n, n))

    for i in np.arange(n):
        for j in np.arange(n):
            L[j, i] = A[i, j]
    return L


def substuicao_frente(L, b):
    n = np.shape(L)[0]
    for j in np.arange(n):
        pivo = b[j]
        for i in np.arange(n):
            if(i > j):
                b[i] += (L[i, j]*-1) * pivo

    return(b)

# Sample symmetric, postive matrix
