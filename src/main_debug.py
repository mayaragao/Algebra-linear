import numpy as np
import Decomposicao_LU as lu
import Cholesky as cy

A = np.matrix([[1, -4, 6, -4], [0, 1, -4, 5],
               [5, -4, 1, 0], [-4, 6, -4, 1]], dtype=float)

A2 = np.matrix([[5, -4, 1, 0], [-4, 6, -4, 1],
                [1, -4, 6, -4], [0, 1, -4, 5]], dtype=float)

A3 = np.matrix([[16, 9, 8, 7, 6, 5, 4, 3, 2, 1],
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

B2 = np.array([-1, 2, 1, 3], dtype=float)

B3 = np.array([4, 0, 8, 0, 2, 0, 8, 0, 4, 0], dtype=float)

#print("A =\n", A, "\nB=\n", B)

L, U = lu.decomposicaoLU(A3)

lu.arredondando(L, 3)
lu.arredondando(U, 3)

print("Matriz L=\n", L, "\nMatriz U=\n", U, "\nA=\n", A3)

det_A = lu.determinante(U)
print("O determinant e de A é :", det_A)

Y = lu.substuicao_frente(L, B3)
X = lu.retro_substituicao(U, Y)

print("Substituiçao pra frente de L e B: \nY= \n", Y, "\nB=\n", B3)
print("Retro-Substituiçao de U e Y: \nU= \n", U, "\nX=\n", X)

C = cy.cholesky(A3)
Ct = cy.transposta(C)

Ych = lu.substuicao_frente(C, B3)
Xch = lu.retro_substituicao(Ct, Ych)

lu.arredondando(C, 3)
lu.arredondando(Ct, 3)

print("\n Decomposição de cholesky:\nMatriz L=\n", C, "\nMatriz L^T=\n", Ct)
print("Substituiçao pra frente de L e B: \nY= \n", Ych, "\nB3=\n", B3)
print("Retro-Substituiçao de L^T e Y: \nL^t= \n", Ct, "\nX=\n", Xch)
