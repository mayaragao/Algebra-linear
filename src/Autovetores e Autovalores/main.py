import numpy as np
import PowerMethod as pm

A = np.matrix([[1, 0.2, 0],
               [0.2, 1, 0.5],
               [0, 0.5, 1]], dtype=float)

n = np.shape(A)[0]
X0 = np.ones(n)
lambda0 = 1
tolerancia = 0.001

print('A:\n', A, '\nx0\n:', X0)


lamb, X, iteracoes = pm.metodo_potencia(A, X0, lambda0, tolerancia)

print('\nAutoVetor = ', X, '\nAutoValor =',
      lamb, '\nNº de iteracoes: ', iteracoes)
