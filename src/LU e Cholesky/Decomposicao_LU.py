import numpy as np


def decomposicaoLU(A):
    boo = matrizQuadrada(A)

    if boo:
        U = np.copy(A)  # Copia pra os elementos de A para U
        n = np.shape(U)[0]  # Recebe o tamanho numero de linhas
        # Cria uma matriz com 1 na diagonal principal e zero nos outros pontos
        L = np.eye(n)

        for j in np.arange(n-1):
            for i in np.arange(j+1, n):
                # divide o elemento abaixo do pivo pelo pivo, e adiciona em L,
                #  simulando aqui uma inversa de uma Matriz de combinação de linhas
                if U[j, j] == 0:
                    # para identificar matrizes singulares ao final
                    boo = False
                L[i, j] = U[i, j]/U[j, j]
                for k in np.arange(j+1, n):
                    # multiplica U pelos valores de L encontrados anteriormente
                    U[i, k] = U[i, k] - L[i, j]*U[j, k]
                U[i, j] = 0  # adiciona 0 em todos elementos abaixo do pivo de U
        if not boo:
            L = np.zeros(1)
            U = np.eye(1)
        return(L, U)


def matrizQuadrada(A):
    n = np.shape(A)[0]  # Recebe o numero de linhas
    m = np.shape(A)[1]  # Recebe o numero de colunas
    if n != m:
        return False
    return True


def substuicao_frente(L, b):
    n = np.shape(L)[0]
    y = np.zeros(n)

    for i in np.arange(n):
        soma = sum(L[i, j] * y[j] for j in np.arange(i))
        y[i] = (b[i] - soma) / L[i, i]
    return(y)


def retro_substituicao(U, y):
    n = np.shape(U)[0]
    x = np.zeros(y.shape)
    x[n-1] = y[n-1]/U[n-1, n-1]

    for i in np.arange(n-2, -1, -1):  # Por linha em forma descrescente
        soma = 0
        for j in np.arange(n):  # por coluna
            soma += U[i, j] * x[j]
        x[i] = (y[i] - soma)/U[i, i]

    return(x)

# calcula o determinante de uma matriz triangular


def determinante(A):
    n = np.shape(A)[0]  # Recebe o numero de linhas
    det = 1
    for i in np.arange(n):
        det *= A[i, i]
    return det


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
                # arredonda cada valor com 1 casa decimal
                A[i, j] = round(A[i, j], x)
