import numpy as np

A = np.matrix([[1, -4, 6, -4], [0, 1, -4, 5],
               [5, -4, 1, 0], [-4, 6, -4, 1]], dtype=float)

B = np.array([1, 3, -1, 2], dtype=float)

A2 = np.matrix([[16, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                [9, 17, 9, 8, 7, 6, 5, 4, 3, 2],
                [8, 9, 18, 9, 8, 7, 6, 5, 4, 3],
                [7, 8, 9, 19, 9, 8, 7, 6, 5, 4],
                [6, 7, 8, 9, 18, 9, 8, 7, 6, 5],
                [5, 6, 7, 8, 9, 17, 9, 8, 7, 6],
                [4, 5, 6, 7, 8, 9, 16, 9, 8, 7],
                [3, 4, 5, 6, 7, 8, 9, 15, 9, 8],
                [2, 3, 4, 5, 6, 7, 8, 9, 14, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]], dtype=float)

print("A =\n", A, "\nB=\n", B)


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
            L = np.eye(1)
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
    y = np.copy(b)
    print("\n Y inicial=\n", y)
    # cria um vetor y copia de b
    for j in np.arange(n):
        pivo = y[j]
        for i in np.arange(n):
            if(i > j):
                # somatorio da substuiçao pra frente
                y[i] += (L[i, j]*-1) * pivo
    return(y)
# calcula o determinante de uma matriz triangular


def retro_substituicao(U, y):
    n = np.shape(U)[0]
    x = np.zeros(y.shape)
    x[n-1] = y[n-1]/U[n-1, n-1]

    for i in np.arange(n-2, -1, -1):  # Por linha em forma descrescente
        soma = 0
        for j in np.arange(n):  # por coluna coluna
            soma += U[i, j] * x[j]
        x[i] = (y[i] - soma)/U[i, i]

    return(x)


def determinante(A):
    n = np.shape(A)[0]  # Recebe o numero de linhas
    det = 1
    for i in np.arange(n):
        det *= A[i, i]
    return det


def arredondando(A):
    n = np.shape(A)[0]
    m = np.shape(A)[1]
    for i in np.arange(n):
        for j in np.arange(m):
            # arredonda cada valor com 1 casa decimal
            A[i, j] = round(A[i, j], 1)


L, U = decomposicaoLU(A)
det_A = determinante(U)
# arredondando(L)
# arredondando(U)
print("Matriz L=\n", L, "\nMatriz U=\n", U, "\nA=\n", A)
print("O determinante de A é :", det_A)

Y = substuicao_frente(L, B)
X = retro_substituicao(U, Y)
print("Substituiçao pra frente de L e B: Y= \n", Y, "\nB=\n", B)
print("Retro-Substituiçao de U e Y: U= \n", U, "\nX=\n", X)
