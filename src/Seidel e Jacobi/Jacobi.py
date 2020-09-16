import numpy as np

A2 = np.matrix([[5, -4, 1, 0], [-4, 6, -4, 1],
                [1, -4, 6, -4], [0, 1, -4, 5]], dtype=float)

B2 = np.array([-1, 2, 1, 3], dtype=float)

A = np.matrix([[10, 2, 1],
               [1, 5, 1],
               [2, 3, 10]], dtype=float)

B = np.array([7, -8, 6], dtype=float)

v0 = np.array([1, 1, 1], dtype=float)
v1 = np.array([1, 1.33, 1.11], dtype=float)
v2 = np.array([1.15, 1.42, 1.19], dtype=float)

Vetor = np.zeros_like(B2)
print('vetor inicial:\n', Vetor)


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


boolean = criterio_convergencia(A2)
print(A2, boolean)


def residuo(v1, v0):
    n = np.shape(v1)[0]
    print("numero linhas de v1 : \n ", n)
    num, den = 0, 0

    for i in np.arange(n):
        num += (v1[i]-v0[i])**2
        den += (v1[i])**2

    num = num**0.5
    den = den**0.5

    r = num/den

    return r


def jacobi(A, b, vetorSolucao, tolerancia, iteracoes):
    iteracao = 0

    boolean = criterio_convergencia(A)
    if (boolean == False):
        return (vetorSolucao, boolean, iteracao)

    vetorAuxiliar = np.copy(vetorSolucao)
    n = np.shape(A)[0]

    while (iteracao < iteracoes):
        for i in np.arange(n):
            x = b[i]
            for j in np.arange(n):
                if (i != j):
                    x -= A[i, j]*vetorSolucao[j]
            x /= A[i, i]
            vetorAuxiliar[i] = x
        iteracao += 1

        vetorSolucao = np.copy(vetorAuxiliar)
        print('\nVetorSolucao da iteracao ', iteracao, ' :\n', vetorSolucao)

    return (vetorSolucao, boolean, iteracao)


r = residuo(v1, v0)
print('residuo de V1 e v2:\n', r)

tolerancia = 0.001

Vetor, boolean, it = jacobi(A2, B2, Vetor, tolerancia, 20)

print('JACOBI:\n vetor:\n ', Vetor, boolean, 'numero iteracoes:\n', it)
