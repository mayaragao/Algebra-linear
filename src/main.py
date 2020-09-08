import numpy as np
import Decomposicao_LU as lu

A = np.matrix([[1, -4, 6, -4], [0, 1, -4, 5],
               [5, -4, 1, 0], [-4, 6, -4, 1]], dtype=float)

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

B = np.array([1, 3, -1, 2], dtype=float)

print("A =\n", A, "\nB=\n", B)

L, U = lu.decomposicaoLU(A)
print("Matriz L=\n", L, "\nMatriz U=\n", U, "\nA=\n", A)

det_A = lu.determinante(U)
print("O determinante de A é :", det_A)

Y = lu.substuicao_frente(L, B)
X = lu.retro_substituicao(U, Y)

print("Substituiçao pra frente de L e B: \nY= \n", Y, "\nB=\n", B)
print("Retro-Substituiçao de U e Y: \nU= \n", U, "\nX=\n", X)
