import numpy as np


def modulo(x):
    if (x < 0):
        return (-x)
    return x


def residuo(l0, l1):
    r = l1 - l0
    r = modulo(r)
    d = modulo(l1)
    r /= d
    return r


def mult_AX(A, X):
    # multiplica matriz A pelo vetor X e retorna vetor Y
    Y = np.zeros_like(X)
    n = np.shape(A)[0]

    for i in np.arange(n):
        soma = 0
        for j in np.arange(n):
            soma += A[i, j] * X[j]
        Y[i] = soma

    return Y


def metodo_potencia(A, X, lamb, tolerancia):
    Y = np.zeros_like(X)
    n = np.shape(A)[0]
    r = 1
    lamb_aux = lamb
    iteracao = 0

    #print('\nX', iteracao, ' = ', X, '   lambda=', lamb)

    while (r > tolerancia):
        iteracao += 1
        Y = mult_AX(A, X)
        lamb_aux = Y[0]

        for i in np.arange(n):
            Y[i] /= lamb_aux
        r = residuo(lamb, lamb_aux)
        #print('\nX', iteracao, ' = ', Y, 'lambda = ', lamb_aux)
        lamb = lamb_aux
        X = np.copy(Y)

    return (lamb, X, iteracao)
