import numpy as np
import Jacobi as jc
import Seidel as sd

A = np.matrix([[10, 2, 1],
               [1, 5, 1],
               [2, 3, 10]], dtype=float)

B = np.array([7, -8, 6], dtype=float)


A2 = np.matrix([[5, -4, 1, 0], [-4, 6, -4, 1],
                [1, -4, 6, -4], [0, 1, -4, 5]], dtype=float)

B2 = np.array([-1, 2, 1, 3], dtype=float)

A3 = np.matrix([[3, 2, 0], [2, 3, -1], [0, -1, 3]], dtype=float)


B3 = np.array([1, -1, 1], dtype=float)


tol = 0.1


def menu(A, B):
    escolha = int(input('''
**********************************************************************

      Solução de AX=B pelos métodos iterativos:
      Qual método deseja utilizar?
        1   Gauss-Jacobi
        2   Gauss-Seidel
        0   Para sair do menu
      Escolha:    '''))
    if escolha == 1:

        Vetor = np.zeros_like(B)

        print('\n GAUSS-JACOBI:\n\n A=\n', A)

        V_jacobi, boolean, it = jc.jacobi(A, B, Vetor, tol)

        if (boolean == False):
            print(
                '\n JACOBI:\n Matriz não é diagonal dominante! \n\n Nº iteracoes:', it)
        else:
            print('JACOBI:\n Vetor:\n ', V_jacobi, '\n\n Matriz é diagonal dominante: ',
                  boolean, '\n Nº iteracoes:', it)

        menu(A, B)
        # pass
    elif escolha == 2:

        Vetor = np.zeros_like(B)
        print('\n METODO DE JACOBI: \n')

        V_seidel, boolean, it = sd.seidel(A, B, Vetor, tol)

        if (boolean == False):
            print(
                '\n SEIDEL:\n A matriz não é diagonal dominante! \n\n Nº iteracoes:', it)
        else:
            print(' SEIDEL:\n Vetor:\n ', V_seidel, '\n\n Matriz é diagonal dominante: ',
                  boolean, '\n Nº iteracoes:', it)

        menu(A, B)
    elif escolha == 0:
        pass
    else:
        print("\nEste número não está nas alternativas, tente novamente :D.", sep='')
        menu(A.B)


menu(A2, B2)
