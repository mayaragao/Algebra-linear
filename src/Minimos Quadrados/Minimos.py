import numpy as np


def minimos_quadrados(X, Y, pontos):

    A = np.zeros((2, 2))
    C = np.zeros(2)
#    H = np.ones((2, pontos))

    for i in np.arange(pontos):
        A[0, 0] += 1
        A[0, 1] += X[i]
        A[1, 0] += X[i]
        A[1, 1] += (X[i]) * (X[i])
        C[0] += Y[i]
        C[1] += (Y[i] * X[i])

    B = np.linalg.solve(A, C)

    print("\n Matriz A =\n", A, '\nC = \n', C, '\n\nSolucao B = \n', B)
    print("\n AJUSTE:\n y(x) = ", round(
        B[0], 3), ' + ', round(B[1], 3), 'x \n')
    return 0
