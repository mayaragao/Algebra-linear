import numpy as np
import PowerMethod as pm
import JacobiMethod as jm


A = np.matrix([[1, 0.2, 0], [0.2, 1, 0.5], [0, 0.5, 1]], dtype=float)


A2 = np.matrix([[3, 2, 0], [2, 3, -1], [0, -1, 3]], dtype=float)


lambda0 = 1
tolerancia = 0.001


def menu(A):
    escolha = int(input('''
**********************************************************************
      
      Cálculo de Autovetores de autovetores e autovalores:
      Qual método deseja utilizar?
        1   Método da Potencia
        2   Método de Jacobi
        0   Para sair do menu
      Escolha:    '''))
    if escolha == 1:

        n = np.shape(A)[0]
        X0 = np.ones(n)

        print('\n MÉTODO DA POTENCIA:\n\n A=\n', A)
        lamb, X, iteracoes = pm.metodo_potencia(A, X0, lambda0, tolerancia)

        print('\n AutoVetor = ', X, '\n AutoValor =',
              lamb, '\n\n Nº de iterações: ', iteracoes, '\n Tolerância: ', tolerancia)

        menu(A)
        # pass
    elif escolha == 2:

        print('\n METODO DE JACOBI: \n')
        Ax, X, iteracoes, boo = jm.metodo_jacobi(A, tolerancia)

        if (boo == False):
            print('\n         A matriz não é simetrica! ')
        else:

            jm.arredondando(X, 4)
            jm.arredondando(A, 4)

            print('\n A =\n', A, '\n\n Matriz Autovetores X = \n', X, '\n Autovalores =\n',
                  Ax, '\n\n Nº de iterações: ', iteracoes, '\n Tolerância: ', tolerancia)

        menu(A)
    elif escolha == 0:
        pass
    else:
        print("\nEste número não está nas alternativas, tente novamente :D.", sep='')
        menu(A)


menu(A2)
