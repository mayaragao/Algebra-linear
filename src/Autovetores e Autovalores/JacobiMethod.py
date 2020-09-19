
import numpy as np
from math import cos, sin, atan, pi


def modulo(x):
    if (x < 0):
        return (-x)
    return x


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
        return (A, False)
    At = transposta(A)

    for i in np.arange(n):
        for j in np.arange(n):
            if (At[i, j] != A[i, j]):
                return (At, False)

    return (At, True)


def teste_convergencia(A, n, tolerancia):
    # analisa se os termos fora da diagonal sao menores que a tolerancia
    # assume que a matriz é simétrica, portanto quadrada

    linha, coluna = 0, 1

    boolean = True
    for i in np.arange(n):
        for j in np.arange(i+1, n):
            a = modulo(A[i, j])
            if (a > tolerancia):
                boolean = False
                if (a > modulo(A[linha, coluna])):
                    linha = i
                    coluna = j

    return (boolean, linha, coluna)
    # retorna True no caso de todos serem menores que a tolerancia
    # senao retorna Falso e o maior elemento fora da diagonal


def angulo_phi(A, i, j):
    if (A[i, i] == A[j, j]):
        phi = (pi / 4)
        return phi

    phi = atan((2*A[j, i])/(A[i, i] - A[j, j]))
    phi /= 2
    return phi


def matriz_rotacao(n, phi, i, j):
    I = np.eye(n)
    I[i, i] = cos(phi)
    I[j, j] = cos(phi)
    I[i, j] = -sin(phi)
    I[j, i] = sin(phi)
    return I


def metodo_jacobi(A, tolerancia):
    Aux = np.copy(A)
    n = np.shape(A)[0]
    X = np.eye(n)
    P = np.eye(n)
    iteracao = 0

    At, boo = simetrica(A)
    if boo == False:
        return (A, X, iteracao, boo)

    ok, linha, coluna = teste_convergencia(Aux, n, tolerancia)

    while (ok == False):
        ok, linha, coluna = teste_convergencia(Aux, n, tolerancia)

        phi = angulo_phi(Aux, linha, coluna)
        P = matriz_rotacao(n, phi, linha, coluna)
        P_t = transposta(P)

        Aux = np.dot(P_t, Aux)
        Aux = np.dot(Aux, P)

        X = np.dot(X, P)
        iteracao += 1

        # print('\n Iteracao nº ', iteracao, '\nangulo phi: ', phi,
        #      '\nmatriz autovalores A=\n', Aux, '\nmatriz Autovetores X=\n', X)

    return (Aux, X, iteracao, ok)


def arredondando(A, x):
    n = np.shape(A)
    aux = len(n)

    n = np.shape(A)[0]

    if aux == 1:
        for i in np.arange(n):
            A[i] = round(A[i], x)
    else:
        m = np.shape(A)[1]
        for i in np.arange(n):
            for j in np.arange(m):
                A[i, j] = round(A[i, j], x)
