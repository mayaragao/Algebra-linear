import numpy as np
import Jacobi as jc


def seidel(A, b, vetorSolucao, tolerancia):
    iteracao = 0

    boolean = jc.criterio_convergencia(A)
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
                    x -= A[i, j]*vetorAuxiliar[j]
            x /= A[i, i]
            vetorAuxiliar[i] = x
        iteracao += 1

        res = jc.residuo(vetorAuxiliar, vetorSolucao)
        vetorSolucao = np.copy(vetorAuxiliar)
        print('\n VetorSolucao da iteracao ', iteracao, ' :\n', vetorSolucao)

    return (vetorSolucao, boolean, iteracao)
