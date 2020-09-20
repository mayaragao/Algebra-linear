import numpy as np
import Minimos as mq


def menu():
    pontos = int(input('''
**********************************************************************

    Minimos Quadrados:

    Quantos pontos deseja usar no ajuste?

    Escolha: '''))
    if (pontos <= 1):
        print('Escolha pelo menos 2 pontos')
        menu()
    X, Y = np.zeros(pontos), np.zeros(pontos)
    for i in np.arange(pontos):
        X[i] = float(input("X" + str(i) + " = "))
        Y[i] = float(input("Y" + str(i) + " = "))

    m = mq.minimos_quadrados(X, Y, pontos)

    return 0


menu()
