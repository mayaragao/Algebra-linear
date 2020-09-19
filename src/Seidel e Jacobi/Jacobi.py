import numpy as np


def modulo(x):
    if (x < 0):
        return (-x)
    return x


def criterio_convergencia(A):
    boo = True
    n = np.shape(A)[0]
    m = np.shape(A)[1]
    if (n != m):
        boo = False
        return boo  # nao converge

    for i in np.arange(n):
        somai, somaj = 0, 0
        for j in np.arange(n):
            if (i != j):
                lin = modulo(A[i, j])
                col = modulo(A[j, i])

                somai += lin
                somaj += col
        a = modulo(A[i, i])

        if ((a < somai) or (a < somaj)):
            boo = False

    return boo


def residuo(v1, v0):
    n = np.shape(v1)[0]
    num, den = 0, 0

    for i in np.arange(n):
        num += (v1[i]-v0[i])**2
        den += (v1[i])**2

    num = num**0.5
    den = den**0.5
    r = num/den

    return r


def jacobi(A, b, vetorSolucao, tolerancia):
    iteracao = 0

    boolean = criterio_convergencia(A)
    if (boolean == False):
        return (vetorSolucao, boolean, iteracao)

    vetorAuxiliar = np.copy(vetorSolucao)
    n = np.shape(A)[0]
    res = 1

    while (res > tolerancia):
        for i in np.arange(n):
            x = b[i]
            for j in np.arange(n):
                if (i != j):
                    x -= A[i, j]*vetorSolucao[j]
            x /= A[i, i]
            vetorAuxiliar[i] = x
        iteracao += 1

        res = residuo(vetorAuxiliar, vetorSolucao)
        vetorSolucao = np.copy(vetorAuxiliar)
        print('\n VetorSolucao da iteracao ', iteracao, ' :\n', vetorSolucao)

    return (vetorSolucao, boolean, iteracao)
