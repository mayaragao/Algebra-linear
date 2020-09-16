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


def menu(A, B):
    escolha = int(input('''
        Qual operação você deseja fazer com A e B ?
1 - Fatoração LU de A
2 - Cholesky de A
3 - Solução de A x = B por LU
4 - Solução de A x = B por Cholesky
5 - Determinante A
0 - Para voltar ao menu
Escolha: '''))
    if escolha == 1:
        L, U = lu.decomposicaoLU(A)

        lu.arredondando(L, 3)
        lu.arredondando(U, 3)

        print(" Decomposição LU:\n Matriz L=\n", L,
              "\nMatriz U=\n", U, "\nMatriz A=\n", A)

        pass
    elif escolha == 2:

        C = cy.cholesky(A)

        Ct = cy.transposta(C)

        lu.arredondando(C, 3)
        lu.arredondando(Ct, 3)

        print("\n Decomposição de cholesky:\nMatriz L=\n",
              C, "\nMatriz L^t=\n", Ct)

        pass
    elif escolha == 3:

        L, U = lu.decomposicaoLU(A)

        Y = cy.substuicao_frente(L, B)
        X = lu.retro_substituicao(U, Y)

        lu.arredondando(L, 3)
        lu.arredondando(U, 3)

        lu.arredondando(X, 3)
        lu.arredondando(Y, 3)

        print("Substituiçao pra frente de L e B: \nY= \n", Y, "\nB=\n", B)
        print("Retro-Substituiçao de U e Y \nU= \n", U, "\nX=\n", X)

        pass

    elif escolha == 4:

        C = cy.cholesky(A)

        Ct = cy.transposta(C)

        Y = cy.substuicao_frente(C, B)
        X = lu.retro_substituicao(Ct, Y)

        lu.arredondando(C, 3)
        lu.arredondando(Ct, 3)

        lu.arredondando(X, 3)
        lu.arredondando(Y, 3)

        print("\n Decomposição de cholesky:\nMatriz L=\n",
              C, "\nMatriz L^t=\n", Ct)
        print("Substituiçao pra frente de L e B: \nY= \n", Y, "\nB=\n", B)
        print("Retro-Substituiçao de U e Y \nL^t= \n", Ct, "\nX=\n", X)

        pass
    elif escolha == 5:
        L, U = lu.decomposicaoLU(A)
        det_A = lu.determinante(U)
        print("O determinante de A é :", det_A)
        pass

    elif escolha == 0:
        pass
    else:
        print("\nEste número não está nas alternativas, tente novamente :D.", sep='')
        menu(A, B)


menu(A3, B3)
